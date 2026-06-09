import sys
import os
from JackTokenizer import JackTokenizer, escape_xml
from CompilationEngine import CompilationEngine

def compile_file(input_file):
    base_name = os.path.splitext(input_file)[0]
    t_xml_out = f"{base_name}T.xml"
    xml_out = f"{base_name}.xml"
    vm_out = f"{base_name}.vm"
    tokenizer_for_xml = JackTokenizer(input_file)
    with open(t_xml_out, 'w') as f:
        f.write("<tokens>\n")
        while tokenizer_for_xml.hasMoreTokens():
            tokenizer_for_xml.advance()
            t_type = tokenizer_for_xml.tokenType()
            if t_type == 'KEYWORD':
                val, tag = tokenizer_for_xml.keyword(), 'keyword'
            elif t_type == 'SYMBOL':
                val, tag = tokenizer_for_xml.symbol(), 'symbol'
            elif t_type == 'IDENTIFIER':
                val, tag = tokenizer_for_xml.identifier(), 'identifier'
            elif t_type == 'INT_CONST':
                val, tag = str(tokenizer_for_xml.intVal()), 'integerConstant'
            elif t_type == 'STRING_CONST':
                val, tag = tokenizer_for_xml.stringVal(), 'stringConstant'
            else:
                continue
            f.write(f"  <{tag}> {escape_xml(str(val))} </{tag}>\n")
        f.write("</tokens>\n")
    print(f"  -> {t_xml_out}")
    tokenizer = JackTokenizer(input_file)
    engine = CompilationEngine(tokenizer, xml_out, vm_out)
    engine.compileClass()
    engine.close()
    print(f"  -> {xml_out}")
    print(f"  -> {vm_out}")


def main():
    if len(sys.argv) != 2:
        sys.exit(1)
    path = sys.argv[1]
    if os.path.isfile(path):
        if not path.endswith('.jack'):
            print(f"{path} is not a .jack file")
            sys.exit(1)
        compile_file(path)
    elif os.path.isdir(path):
        jack_files = [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.jack')]
        if not jack_files:
            print(f"No .jack files found in {path}")
            sys.exit(1)
        for jack_file in sorted(jack_files):
            compile_file(jack_file)
    else:
        print(f"{path} is not a valid file or directory")
        sys.exit(1)

if __name__ == '__main__':
    main()
