VM to Hack Assembly Translator


Functionality:

The translator reads .vm files containing stack-based virtual machine commands and outputs
an .asm file containing the Hack Assembly code for the same. 

It supports the following commands:
Stack Arithmetic and Logical Commands: add, sub, neg, eq, gt, lt, and, or, not
Memory Segments Push and Pop: local, argument, this, that, constant, static, temp, pointer
Program Flow Commands: label, goto, if-goto
Function Calling Commands: function, call, return

Note: When translating a directory of .vm files, the translator automatically injects code to initialize the stack pointer (SP = 256) and
calls the Sys.init function to start program execution.


File Structure:

The main.py file has two primary components:

1. Parser: To read the .vm file, strip out comments and whitespace, and break down each
command into its components (command type, arg 1, arg 2).
2. CodeWriter: Takes the parsed commands and generates the corresponding Hack Assembly
instructions.


Usage:

Single File: If you pass a single .vm file as an argument, it will generate an .asm file in the same directory.
Command: 
python main.py path/to/your/file.vm
Output: path/to/your/file.asm

Directory: If you pass a directory containing multiple .vm files, it will parse all .vm
files within that directory and compile them into a single .asm file named after the directory. 
Command:
python main.py path/to/your/directory
Output: path/to/your/directory/directory.asm


