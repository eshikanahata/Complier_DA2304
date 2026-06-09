import sys
import sys
from parser import Parser
from code import Code
from symbol_table import SymbolTable

class Assembler:
    def __init__(self, file_path):
        self.file_path = file_path
        self.parser = Parser(file_path)
        self.symbol_table = SymbolTable()
        self.code = Code()
        self.ram_address = 16

    def first_pass(self):
        rom_address = 0
        self.parser.current_line = 0
        
        while self.parser.hasMoreLines():
            instruction = self.parser.instruction_type()
            
            if instruction == 0 or instruction == 1:
                rom_address += 1
            elif instruction == 2:
                label = self.parser.symbol()
                if not self.symbol_table.contains(label):
                    self.symbol_table.addEntry(label, rom_address)
                    
            self.parser.advance()

    def second_pass(self):
        self.parser.current_line = 0
        machine_code = []

        while self.parser.hasMoreLines():
            instruction = self.parser.instruction_type()

            if instruction == 0:
                symbol = self.parser.symbol()
                
                if symbol.isdigit():
                    address = int(symbol)
                else:
                    if not self.symbol_table.contains(symbol):
                        self.symbol_table.addEntry(symbol, self.ram_address)
                        self.ram_address += 1
                    address = self.symbol_table.getAddress(symbol)
                
                binary_instruction = f"0{address:015b}"
                machine_code.append(binary_instruction)

            elif instruction == 1:
                dest_bits = self.code.dest(self.parser.dest())
                comp_bits = self.code.comp(self.parser.comp())
                jump_bits = self.code.jump(self.parser.jump())
                
                binary_instruction = f"111{comp_bits}{dest_bits}{jump_bits}"
                machine_code.append(binary_instruction)

            self.parser.advance()

        return machine_code

    def assemble(self):
        self.first_pass()
        machine_code = self.second_pass()
        
        output_path = self.file_path.replace('.asm', '.hack')
        with open(output_path, 'w') as out_file:
            out_file.write('\n'.join(machine_code) + '\n')

if __name__ == "__main__":
    if len(sys.argv) == 2:
        assembler = Assembler(sys.argv[1])
        assembler.assemble()