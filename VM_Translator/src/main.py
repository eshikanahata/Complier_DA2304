import os
import sys

class Parser:
    def __init__(self, filepath):
        self.lines = []
        self.current = None
        self.idx = -1
        with open(filepath, 'r') as f:
            for line in f:
                stripped = line.split('//')[0].strip()
                if stripped:
                    self.lines.append(stripped.split())

    def hasMoreLines(self):
        return self.idx + 1 < len(self.lines)

    def advance(self):
        if self.hasMoreLines():
            self.idx += 1
            self.current = self.lines[self.idx]

    def commandType(self):
        cmd = self.current[0]
        arithmetic = {"add", "sub", "neg", "eq", "gt", "lt", "and", "or", "not"}
        if cmd in arithmetic: return "C_ARITHMETIC"
        if cmd == "push": return "C_PUSH"
        if cmd == "pop": return "C_POP"
        if cmd == "label": return "C_LABEL"
        if cmd == "goto": return "C_GOTO"
        if cmd == "if-goto": return "C_IF"
        if cmd == "function": return "C_FUNCTION"
        if cmd == "call": return "C_CALL"
        if cmd == "return": return "C_RETURN"
        raise ValueError(f"Unknown command: {cmd}")

    def arg1(self):
        if self.commandType() == "C_ARITHMETIC": return self.current[0]
        return self.current[1]

    def arg2(self):
        return int(self.current[2])

class CodeWriter:
    def __init__(self, filepath):
        self.output = open(filepath, 'w')
        self.filename = ""
        self.current_function = ""
        self.label_count = 0
        self.segment_map = {"local": "LCL", "argument": "ARG", "this": "THIS", "that": "THAT"}

    def _clean_write(self, text):
        for line in text.strip().split('\n'):
            line = line.strip()
            if not line: continue
            if line.startswith('('):
                self.output.write(line + "\n")
            else:
                self.output.write(line.replace(" ", "") + "\n")

    def set_filename(self, filename):
        self.filename = os.path.basename(filename).replace(".vm", "")

    def writeInit(self):
        self._clean_write("@256\nD=A\n@SP\nM=D")
        self.writeCall("Sys.init", 0)

    def writeArithmetic(self, command):
        if command in ["add", "sub", "and", "or"]:
            op = {"add":"+", "sub":"-", "and":"&", "or":"|"}[command]
            self._clean_write(f"@SP\nAM=M-1\nD=M\nA=A-1\nM=M{op}D")
        elif command == "neg":
            self._clean_write("@SP\nA=M-1\nM=-M")
        elif command == "not":
            self._clean_write("@SP\nA=M-1\nM=!M")
        elif command in ["eq", "gt", "lt"]:
            jmp = {"eq":"JEQ", "gt":"JGT", "lt":"JLT"}[command]
            label = f"CMP_{self.label_count}"
            self.label_count += 1
            self._clean_write(f"@SP\nAM=M-1\nD=M\nA=A-1\nD=M-D\n@TRUE_{label}\nD;{jmp}\n@SP\nA=M-1\nM=0\n@END_{label}\n0;JMP\n(TRUE_{label})\n@SP\nA=M-1\nM=-1\n(END_{label})")

    def writePushPop(self, command, segment, index):
        if command == "C_PUSH":
            if segment == "constant":
                self._clean_write(f"@{index}\nD=A")
            elif segment in self.segment_map:
                self._clean_write(f"@{self.segment_map[segment]}\nD=M\n@{index}\nA=D+A\nD=M")
            elif segment == "temp":
                self._clean_write(f"@{5+index}\nD=M")
            elif segment == "pointer":
                self._clean_write(f"@{'THIS' if index==0 else 'THAT'}\nD=M")
            elif segment == "static":
                self._clean_write(f"@{self.filename}.{index}\nD=M")
            self._clean_write("@SP\nA=M\nM=D\n@SP\nM=M+1")

        elif command == "C_POP":
            if segment in self.segment_map:
                self._clean_write(f"@{self.segment_map[segment]}\nD=M\n@{index}\nD=D+A\n@R13\nM=D")
            elif segment == "temp":
                self._clean_write(f"@{5+index}\nD=A\n@R13\nM=D")
            elif segment == "pointer":
                self._clean_write(f"@{'THIS' if index==0 else 'THAT'}\nD=A\n@R13\nM=D")
            elif segment == "static":
                self._clean_write(f"@{self.filename}.{index}\nD=A\n@R13\nM=D")
            self._clean_write("@SP\nAM=M-1\nD=M\n@R13\nA=M\nM=D")

    def writeLabel(self, label):
        self.output.write(f"({self.current_function}${label})\n")

    def writeGoto(self, label):
        self._clean_write(f"@{self.current_function}${label}\n0;JMP")

    def writeIf(self, label):
        self._clean_write(f"@SP\nAM=M-1\nD=M\n@{self.current_function}${label}\nD;JNE")

    def writeFunction(self, function_name, num_locals):
        self.current_function = function_name
        self.output.write(f"({function_name})\n")
        for _ in range(num_locals):
            self.writePushPop("C_PUSH", "constant", 0)

    def writeCall(self, function_name, num_args):
        ret_label = f"RET_{self.label_count}"
        self.label_count += 1
        self._clean_write(f"@{ret_label}\nD=A\n@SP\nA=M\nM=D\n@SP\nM=M+1")
        for seg in ["LCL", "ARG", "THIS", "THAT"]:
            self._clean_write(f"@{seg}\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1")
        self._clean_write(f"@SP\nD=M\n@{5+num_args}\nD=D-A\n@ARG\nM=D")
        self._clean_write("@SP\nD=M\n@LCL\nM=D")
        self._clean_write(f"@{function_name}\n0;JMP\n({ret_label})")

    def writeReturn(self):
        self._clean_write("@LCL\nD=M\n@R14\nM=D")
        self._clean_write("@5\nA=D-A\nD=M\n@R15\nM=D")
        self._clean_write("@SP\nAM=M-1\nD=M\n@ARG\nA=M\nM=D")
        self._clean_write("@ARG\nD=M+1\n@SP\nM=D")
        for i, seg in enumerate(["THAT", "THIS", "ARG", "LCL"], 1):
            self._clean_write(f"@R14\nD=M\n@{i}\nA=D-A\nD=M\n@{seg}\nM=D")
        self._clean_write("@R15\nA=M\n0;JMP")

    def close(self):
        self.output.close()

def main():
    if len(sys.argv) < 2: return
    input_path = sys.argv[1].rstrip('/')
    
    if os.path.isdir(input_path):
        output_filepath = os.path.join(input_path, f"{os.path.basename(input_path)}.asm")
        files = [os.path.join(input_path, f) for f in os.listdir(input_path) if f.endswith(".vm")]
        is_dir = True
    else:
        output_filepath = input_path.replace(".vm", ".asm")
        files = [input_path]
        is_dir = False

    writer = CodeWriter(output_filepath)
    if is_dir: writer.writeInit()

    for f in files:
        writer.set_filename(f)
        parser = Parser(f)
        while parser.hasMoreLines():
            parser.advance()
            ctype = parser.commandType()
            if ctype == "C_ARITHMETIC": writer.writeArithmetic(parser.arg1())
            elif ctype in ["C_PUSH", "C_POP"]: writer.writePushPop(ctype, parser.arg1(), parser.arg2())
            elif ctype == "C_LABEL": writer.writeLabel(parser.arg1())
            elif ctype == "C_GOTO": writer.writeGoto(parser.arg1())
            elif ctype == "C_IF": writer.writeIf(parser.arg1())
            elif ctype == "C_FUNCTION": writer.writeFunction(parser.arg1(), parser.arg2())
            elif ctype == "C_CALL": writer.writeCall(parser.arg1(), parser.arg2())
            elif ctype == "C_RETURN": writer.writeReturn()
    writer.close()

if __name__ == "__main__":
    main()
