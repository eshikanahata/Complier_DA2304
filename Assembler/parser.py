class Parser:
    def __init__(self, file_path): 
        self.lines = []
        with open(file_path, 'r') as f:
            for line in f:
                clean_line = line.split('//')[0].replace(" ", "").strip()
                if clean_line: 
                    self.lines.append(clean_line)
        
        self.total_lines = len(self.lines)
        self.current_line = 0
        self.mapping = []

    def hasMoreLines(self):
        return self.current_line < self.total_lines
    
    def advance(self):
        self.current_line += 1
    
    def instruction_type(self): 
        # 0 is for A-instruction, 2 is for L-instruction, and 1 is for C-instruction 
        line = self.lines[self.current_line]
        if line.startswith('@'):
            return 0
        elif line.startswith('(') and line.endswith(')'):
            return 2
        else:
            return 1

    def symbol(self):
        line = self.lines[self.current_line]
        if self.instruction_type() == 0:
            return line[1:].strip()  
        elif self.instruction_type() == 2:
            return line[1:-1].strip() 

    def dest(self):
        line = self.lines[self.current_line]
        if '=' in line:
            return line.split('=')[0].strip() 
        return "null"

    def comp(self):
        line = self.lines[self.current_line]
        if '=' in line:
            line = line.split('=')[1]
        if ';' in line:
            line = line.split(';')[0]
        return line.strip() 

    def jump(self):
        line = self.lines[self.current_line]
        if ';' in line:
            return line.split(';')[1].strip() 
        return "null"

    def orchestrate(self): 
        while self.hasMoreLines():
            instruction = self.instruction_type()
            if instruction == 0 or instruction == 2:
                self.mapping.append([self.symbol()])
            elif instruction == 1:
                self.mapping.append([self.dest(), self.comp(), self.jump()])
            else:
                raise ValueError

            self.advance()    

        return self.mapping