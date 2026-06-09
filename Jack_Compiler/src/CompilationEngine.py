from SymbolTable import SymbolTable
from VMWriter import VMWriter
from JackTokenizer import escape_xml

class CompilationEngine:
    def __init__(self, tokenizer, xml_out, vm_out):
        self.tokenizer = tokenizer
        self.f_xml = open(xml_out, 'w')
        self.vm = VMWriter(vm_out)
        self.symbols = SymbolTable()
        self.class_name = ""
        self.current_sub_name = ""
        self.current_sub_type = ""
        self.label_counter = 0
        self.indent = 0
        if self.tokenizer.hasMoreTokens():
            self.tokenizer.advance()

    def close(self):
        self.f_xml.close()
        self.vm.close()

    def _xml_open(self, tag):
        self.f_xml.write("  " * self.indent + f"<{tag}>\n")
        self.indent += 1

    def _xml_close(self, tag):
        self.indent -= 1
        self.f_xml.write("  " * self.indent + f"</{tag}>\n")

    def forward(self):
        t_type = self.tokenizer.tokenType()
        if t_type == 'KEYWORD':
            val, tag = self.tokenizer.keyword(), 'keyword'
        elif t_type == 'SYMBOL':
            val, tag = self.tokenizer.symbol(), 'symbol'
        elif t_type == 'IDENTIFIER':
            val, tag = self.tokenizer.identifier(), 'identifier'
        elif t_type == 'INT_CONST':
            val, tag = self.tokenizer.intVal(), 'integerConstant'
        elif t_type == 'STRING_CONST':
            val, tag = self.tokenizer.stringVal(), 'stringConstant'
        else:
            raise RuntimeError()
        self.f_xml.write("  " * self.indent + f"<{tag}> {escape_xml(str(val))} </{tag}>\n")
        if self.tokenizer.hasMoreTokens():
            self.tokenizer.advance()
        return val

    def _new_label(self):
        self.label_counter += 1
        return f"L{self.label_counter}"

    def compileClass(self):
        self._xml_open("class")
        self.forward()
        self.class_name = self.forward()
        self.forward()
        while (self.tokenizer.tokenType() == 'KEYWORD' and self.tokenizer.keyword() in ('static', 'field')):
            self.compileClassVarDec()
        while (self.tokenizer.tokenType() == 'KEYWORD' and self.tokenizer.keyword() in ('constructor', 'function', 'method')):
            self.compileSubroutine()
        self.forward()
        self._xml_close("class")

    def compileClassVarDec(self):
        self._xml_open("classVarDec")
        kind = self.forward()
        type_name = self.forward()
        var_name = self.forward()
        self.symbols.define(var_name, type_name, kind)
        while (self.tokenizer.tokenType() == 'SYMBOL' and self.tokenizer.symbol() == ','):
            self.forward()
            var_name = self.forward()
            self.symbols.define(var_name, type_name, kind)
        self.forward()
        self._xml_close("classVarDec")

    def compileSubroutine(self):
        self._xml_open("subroutineDec")
        self.symbols.startSubroutine()
        self.current_sub_type = self.forward()
        self.forward()
        self.current_sub_name = self.forward()
        if self.current_sub_type == 'method':
            self.symbols.define('this', self.class_name, 'argument')
        self.forward()
        self.compileParameterList()
        self.forward()
        self.compileSubroutineBody()
        self._xml_close("subroutineDec")

    def compileParameterList(self):
        self._xml_open("parameterList")
        if not (self.tokenizer.tokenType() == 'SYMBOL' and self.tokenizer.symbol() == ')'):
            type_name = self.forward()
            var_name = self.forward()
            self.symbols.define(var_name, type_name, 'argument')
            while (self.tokenizer.tokenType() == 'SYMBOL' and self.tokenizer.symbol() == ','):
                self.forward()
                type_name = self.forward()
                var_name = self.forward()
                self.symbols.define(var_name, type_name, 'argument')
        self._xml_close("parameterList")

    def compileSubroutineBody(self):
        self._xml_open("subroutineBody")
        self.forward()
        while (self.tokenizer.tokenType() == 'KEYWORD' and self.tokenizer.keyword() == 'var'):
            self.compileVarDec()
        n_locals = self.symbols.varCount('var')
        self.vm.writeFunction(f"{self.class_name}.{self.current_sub_name}", n_locals)
        if self.current_sub_type == 'constructor':
            n_fields = self.symbols.varCount('field')
            self.vm.writePush('constant', n_fields)
            self.vm.writeCall('Memory.alloc', 1)
            self.vm.writePop('pointer', 0)
        elif self.current_sub_type == 'method':
            self.vm.writePush('argument', 0)
            self.vm.writePop('pointer', 0)
        self.compileStatements()
        self.forward()
        self._xml_close("subroutineBody")

    def compileVarDec(self):
        self._xml_open("varDec")
        self.forward()
        type_name = self.forward()
        var_name = self.forward() 
        self.symbols.define(var_name, type_name, 'var')
        while (self.tokenizer.tokenType() == 'SYMBOL' and self.tokenizer.symbol() == ','):
            self.forward()
            var_name = self.forward()
            self.symbols.define(var_name, type_name, 'var')
        self.forward()
        self._xml_close("varDec")

    def compileStatements(self):
        self._xml_open("statements")
        while (self.tokenizer.tokenType() == 'KEYWORD' and self.tokenizer.keyword() in ('let', 'if', 'while', 'do', 'return')):
            kw = self.tokenizer.keyword()
            if   kw == 'let':
                self.compileLet()
            elif kw == 'if':
                self.compileIf()
            elif kw == 'while':
                self.compileWhile()
            elif kw == 'do':
                self.compileDo()
            elif kw == 'return':
                self.compileReturn()
        self._xml_close("statements")

    def compileLet(self):
        self._xml_open("letStatement")
        self.forward()
        var_name = self.forward()
        is_array = False
        if (self.tokenizer.tokenType() == 'SYMBOL' and self.tokenizer.symbol() == '['):
            is_array = True
            self.forward()
            self.vm.writePush(self.symbols.segmentOf(var_name), self.symbols.indexOf(var_name))
            self.compileExpression()
            self.forward()
            self.vm.writeArithmetic("add")
        self.forward()
        self.compileExpression()
        self.forward()
        if is_array:
            self.vm.writePop('temp', 0)
            self.vm.writePop('pointer', 1)
            self.vm.writePush('temp', 0)
            self.vm.writePop('that', 0)
        else:
            self.vm.writePop(self.symbols.segmentOf(var_name), self.symbols.indexOf(var_name))
        self._xml_close("letStatement")

    def compileIf(self):
        self._xml_open("ifStatement")
        self.forward()
        self.forward()
        self.compileExpression()
        self.forward()
        l1 = self._new_label()
        l2 = self._new_label()
        self.vm.writeArithmetic("not")
        self.vm.writeIf(l1)
        self.forward()
        self.compileStatements()
        self.forward()
        self.vm.writeGoto(l2)
        self.vm.writeLabel(l1)
        if (self.tokenizer.tokenType() == 'KEYWORD'
            and self.tokenizer.keyword() == 'else'):
            self.forward()
            self.forward()
            self.compileStatements()
            self.forward()
        self.vm.writeLabel(l2)
        self._xml_close("ifStatement")

    def compileWhile(self):
        self._xml_open("whileStatement")
        l1 = self._new_label()
        l2 = self._new_label()
        self.vm.writeLabel(l1)
        self.forward()
        self.forward()
        self.compileExpression()
        self.forward()
        self.vm.writeArithmetic("not")
        self.vm.writeIf(l2)
        self.forward()
        self.compileStatements()
        self.forward()
        self.vm.writeGoto(l1)
        self.vm.writeLabel(l2)
        self._xml_close("whileStatement")

    def compileDo(self):
        self._xml_open("doStatement")
        self.forward()
        name   = self.forward()
        n_args = 0
        if (self.tokenizer.tokenType() == 'SYMBOL'
                and self.tokenizer.symbol() == '.'):
            self.forward()
            sub_name  = self.forward()
            type_name = self.symbols.typeOf(name)
            if type_name:
                self.vm.writePush(self.symbols.segmentOf(name), self.symbols.indexOf(name))
                func_name = f"{type_name}.{sub_name}"
                n_args += 1
            else:
                func_name = f"{name}.{sub_name}"
        else:
            func_name = f"{self.class_name}.{name}"
            self.vm.writePush('pointer', 0)
            n_args += 1
        self.forward()
        n_args += self.compileExpressionList()
        self.forward()
        self.vm.writeCall(func_name, n_args)

        self.forward()
        self.vm.writePop('temp', 0)
        self._xml_close("doStatement")

    def compileReturn(self):
        self._xml_open("returnStatement")
        self.forward()
        if not (self.tokenizer.tokenType() == 'SYMBOL'
                and self.tokenizer.symbol() == ';'):
            self.compileExpression()
        else:
            self.vm.writePush('constant', 0)
        self.forward()
        self.vm.writeReturn()
        self._xml_close("returnStatement")

    def compileExpression(self):
        self._xml_open("expression")
        self.compileTerm()
        binary_ops = frozenset(['+', '-', '*', '/', '&', '|', '<', '>', '='])
        while (self.tokenizer.tokenType() == 'SYMBOL' and self.tokenizer.symbol() in binary_ops):
            op = self.forward()
            self.compileTerm()
            if op == '+':
                self.vm.writeArithmetic('add')
            elif op == '-':
                self.vm.writeArithmetic('sub')
            elif op == '&':
                self.vm.writeArithmetic('and')
            elif op == '|':
                self.vm.writeArithmetic('or')
            elif op == '<':
                self.vm.writeArithmetic('lt')
            elif op == '>':
                self.vm.writeArithmetic('gt')
            elif op == '=':
                self.vm.writeArithmetic('eq')
            elif op == '*':
                self.vm.writeCall('Math.multiply', 2)
            elif op == '/':
                self.vm.writeCall('Math.divide', 2)
        self._xml_close("expression")

    def compileTerm(self):
        self._xml_open("term")
        t_type = self.tokenizer.tokenType()
        if t_type == 'INT_CONST':
            val = self.forward()
            self.vm.writePush('constant', val)
        elif t_type == 'STRING_CONST':
            string_val = self.forward()
            self.vm.writePush('constant', len(string_val))
            self.vm.writeCall('String.new', 1)
            for ch in string_val:
                self.vm.writePush('constant', ord(ch))
                self.vm.writeCall('String.appendChar', 2)
        elif t_type == 'KEYWORD':
            kw = self.forward()
            if kw == 'this':
                self.vm.writePush('pointer', 0)
            elif kw in ('false', 'null'):
                self.vm.writePush('constant', 0)
            elif kw == 'true':
                self.vm.writePush('constant', 1)
                self.vm.writeArithmetic('neg')
        elif t_type == 'SYMBOL':
            sym = self.tokenizer.symbol()
            if sym in ('-', '~'):
                self.forward()
                self.compileTerm()
                self.vm.writeArithmetic('neg' if sym == '-' else 'not')
            elif sym == '(':
                self.forward()
                self.compileExpression()
                self.forward()
        elif t_type == 'IDENTIFIER':
            name = self.forward()
            next_sym = (self.tokenizer.symbol()
                        if self.tokenizer.tokenType() == 'SYMBOL' else None)
            if next_sym == '[':
                self.forward()
                self.vm.writePush(self.symbols.segmentOf(name), self.symbols.indexOf(name))
                self.compileExpression()
                self.forward()
                self.vm.writeArithmetic("add")
                self.vm.writePop('pointer', 1)
                self.vm.writePush('that', 0)
            elif next_sym in ('(', '.'):
                n_args = 0
                if next_sym == '.':
                    self.forward()
                    sub_name  = self.forward()
                    type_name = self.symbols.typeOf(name)
                    if type_name:
                        self.vm.writePush(self.symbols.segmentOf(name), self.symbols.indexOf(name))
                        func_name = f"{type_name}.{sub_name}"
                        n_args += 1
                    else:
                        func_name = f"{name}.{sub_name}"
                else:
                    func_name = f"{self.class_name}.{name}"
                    self.vm.writePush('pointer', 0)
                    n_args += 1
                self.forward()
                n_args += self.compileExpressionList()
                self.forward()
                self.vm.writeCall(func_name, n_args)
            else:
                self.vm.writePush(self.symbols.segmentOf(name), self.symbols.indexOf(name))
        self._xml_close("term")

    def compileExpressionList(self):
        self._xml_open("expressionList")
        n_args = 0
        if not (self.tokenizer.tokenType() == 'SYMBOL' and self.tokenizer.symbol() == ')'):
            self.compileExpression()
            n_args += 1
            while (self.tokenizer.tokenType() == 'SYMBOL' and self.tokenizer.symbol() == ','):
                self.forward()
                self.compileExpression()
                n_args += 1
        self._xml_close("expressionList")
        return n_args
