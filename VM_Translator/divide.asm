@256 
D = A 
@SP 
M = D 
@13 
D = A 
@SP 
A = M 
M = D 
@SP 
M = M + 1 
@5 
D = A 
@SP 
A = M 
M = D 
@SP 
M = M + 1 
@divide.op_RETURN_0 
D = A 
@SP 
A = M 
M = D 
@SP 
M = M + 1 
@LCL 
D = M 
@SP 
A = M 
M = D 
@SP 
M = M + 1 
@ARG 
D = M 
@SP 
A = M 
M = D 
@SP 
M = M + 1 
@THIS 
D = M 
@SP 
A = M 
M = D 
@SP 
M = M + 1 
@THAT 
D = M 
@SP 
A = M 
M = D 
@SP 
M = M + 1 
@SP 
D = M 
@7 
D = D - A 
@ARG 
M = D 
@SP 
D = M 
@LCL 
M = D 
@divide.op 
0;JMP 
(divide.op_RETURN_0)
(END_FINAL)
@END_FINAL 
0;JMP 
(divide.op)
@0 
D = A 
@SP 
A = M 
M = D 
@SP 
M = M + 1 
@0 
D = A 
@SP 
A = M 
M = D 
@SP 
M = M + 1 
@LCL 
D = M 
@0 
D = D + A 
@R13 
M = D
@SP 
AM = M - 1 
D = M 
@R13 
A = M 
M = D 
(divide.op$LOOP)
@ARG 
D = M 
@0 
A = D + A 
D = M 
@SP 
A = M 
M = D 
@SP 
M = M + 1 
@ARG 
D = M 
@1 
A = D + A 
D = M 
@SP 
A = M 
M = D 
@SP 
M = M + 1 
@SP 
AM = M - 1 
D = M 
A = A - 1 
D = M - D 
@LT_LABEL_1_TRUE 
D;JLT 
@SP 
A = M - 1 
M=0 
@LT_LABEL_1_END 
0;JMP 
(LT_LABEL_1_TRUE) 
@SP 
A = M - 1 
M = -1 
(LT_LABEL_1_END) 
@SP 
AM = M - 1 
D = M 
@divide.op$END_DIV 
D;JNE 
@ARG 
D = M 
@0 
A = D + A 
D = M 
@SP 
A = M 
M = D 
@SP 
M = M + 1 
@ARG 
D = M 
@1 
A = D + A 
D = M 
@SP 
A = M 
M = D 
@SP 
M = M + 1 
@SP 
AM = M - 1 
D = M 
A = A - 1 
M = M - D 
@ARG 
D = M 
@0 
D = D + A 
@R13 
M = D
@SP 
AM = M - 1 
D = M 
@R13 
A = M 
M = D 
@LCL 
D = M 
@0 
A = D + A 
D = M 
@SP 
A = M 
M = D 
@SP 
M = M + 1 
@1 
D = A 
@SP 
A = M 
M = D 
@SP 
M = M + 1 
@SP 
AM = M - 1 
D = M 
A = A - 1 
M = D + M 
@LCL 
D = M 
@0 
D = D + A 
@R13 
M = D
@SP 
AM = M - 1 
D = M 
@R13 
A = M 
M = D 
@divide.op$LOOP 
0;JMP 
(divide.op$END_DIV)
@ARG 
D = M 
@0 
A = D + A 
D = M 
@SP 
A = M 
M = D 
@SP 
M = M + 1 
@5 
D = A 
@R13 
M = D 
@SP 
AM = M - 1 
D = M 
@R13 
A = M 
M = D 
@LCL 
D = M 
@0 
A = D + A 
D = M 
@SP 
A = M 
M = D 
@SP 
M = M + 1 
@LCL 
D = M 
@R14 
M = D 
@5 
A = D - A 
D = M 
@R15 
M = D 
@SP 
AM = M - 1 
D = M 
@ARG 
A = M 
M = D 
@ARG 
D = M + 1 
@SP 
M = D 
@R14 
D = M 
@1 
A = D - A 
D = M 
@THAT 
M = D 
@R14 
D = M 
@2 
A = D - A 
D = M 
@THIS 
M = D 
@R14 
D = M 
@3 
A = D - A 
D = M 
@ARG 
M = D 
@R14 
D = M 
@4 
A = D - A 
D = M 
@LCL 
M = D 
@R15 
A = M 
0;JMP 
