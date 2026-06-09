# Jack Compiler


## Pipeline

Conv.jack and Main.jack
        │
        ▼
  JackTokenizer        →  ConvT.xml, MainT.xml (token stream)
        │
        ▼
 CompilationEngine     →  Conv.xml, Main.xml (parse tree)
        │
        ▼
    VMWriter           →  Conv.vm, Main.vm (VM code)
        │
        ▼
  VM Emulator           
        │
        ▼
  VM Translator        →  out.asm (Hack assembly)
        │
        ▼
  CPU Emulator


## Requirements

- Python 3+


## File descriptions

| File | Role |
|------|------|
| JackTokenizer.py | Strips comments/whitespace and tokenises a .jack file into keywords, symbols, identifiers, integer constants, and string constants |
| SymbolTable.py | Symbol table (class level as well as subroutine level) that maps each identifier to its type, kind, and index |
| VMWriter.py | Writes VM commands to a .vm file |
| CompilationEngine.py | Consumes tokens from the tokeniser, emits an XML parse tree, and drives the VMWriter to produce VM code |
| JackCompiler.py | Accepts a single .jack file or a directory and orchestrates the above modules |


## How to run

All five compiler files must be in the same folder as the .jack files. Navigate to the folder and run:

### Compile a single file

python3 JackCompiler.py Conv.jack
python3 JackCompiler.py Main.jack

Conv.jack  
- ConvT.xml   (token stream XML)
- Conv.xml    (parse tree XML)
- Conv.vm     (VM code)


### Compile a directory

python3 JackCompiler.py path/to/jack_folder/

This iterates over every .jack file in the folder and produces the same three output files per class.


### Translate VM to Hack assembly

Run the VM translator on the folder containing the .vm output files: (main.py from Assignment 2)

python3 main.py <vm_files_output_folder>


