@i
M = 0
@j
M = 0
@k
M = 0

@100     
D = A    
@baseA  
M = D    

@200
D = A
@baseB
M = D

@300
D = A
@baseC
M = D

(I_LOOP)
    @i
    D = M
    @3
    D = D - A

    @END
    D;JEQ

    @j
    M = 0

    (J_LOOP)
        @j
        D = M
        @3
        D = D - A

        @INC_I
        D;JEQ

        @k
        M = 0
        @sum
        M = 0

        (K_LOOP)
            @k
            D = M
            @3
            D = D - A

            @SAVE
            D;JEQ

            @baseA
            D = M
            @k
            D = D + M
            @i
            D = D + M
            D = D + M
            D = D + M
            @a_addr
            M = D

            @baseB
            D = M
            @j
            D = D + M
            @k
            D = D + M
            D = D + M
            D = D + M
            @b_addr
            M = D

            @a_addr
            A = M
            D = M
            @val_a
            M = D

            @b_addr
            A = M
            D = M
            @val_b
            M = D

            
            @val_b
            D = M
            @temp_b
            M = D

            (MULT_LOOP)
                @temp_b
                D = M
                @MULT_END
                D;JEQ

                @val_a
                D = M
                @sum
                M = D + M

                @temp_b
                M = M - 1

                @MULT_LOOP
                0;JMP

            (MULT_END)

            @k
            M = M + 1
            @K_LOOP
            0;JMP

        (SAVE)
        @baseC
        D = M
        @j
        D = D + M
        @i
        D = D + M
        D = D + M
        D = D + M
        @c_addr
        M = D

        @sum
        D = M
        @c_addr
        A = M
        M = D

        @j
        M = M + 1
        @J_LOOP
        0;JMP

    (INC_I)
    @i
    M = M + 1
    @I_LOOP
    0;JMP

(END)
@END
0;JMP


