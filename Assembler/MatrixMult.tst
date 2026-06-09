load MatrixMult.hack,
output-file MatrixMult.out,
compare-to MatrixMult.cmp,

output-list RAM[300]%D1.6.1 RAM[301]%D1.6.1 RAM[302]%D1.6.1 RAM[303]%D1.6.1 RAM[304]%D1.6.1 RAM[305]%D1.6.1 RAM[306]%D1.6.1 RAM[307]%D1.6.1 RAM[308]%D1.6.1;

set RAM[100] 1,
set RAM[101] 2,
set RAM[102] 3,
set RAM[103] 4,
set RAM[104] 5,
set RAM[105] 6,
set RAM[106] 7,
set RAM[107] 8,
set RAM[108] 9,

set RAM[200] 2,
set RAM[201] 0,
set RAM[202] 0,
set RAM[203] 0,
set RAM[204] 2,
set RAM[205] 0,
set RAM[206] 0,
set RAM[207] 0,
set RAM[208] 2,


repeat 50000 {
  ticktock;
}

output;
