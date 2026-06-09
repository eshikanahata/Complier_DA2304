load ALU.hdl,
output-file ALU.out,
compare-to ALU.cmp,
output-list x%B1.16.1 y%B1.16.1 zx%B1.1.1 nx%B1.1.1 zy%B1.1.1 ny%B1.1.1 f%B1.1.1 no%B1.1.1 out%B1.16.1 zr%B1.1.1 ng%B1.1.1;


set x %B0000000000000000,
set y %B0000000000000000,

set zx 1, set nx 1, set zy 1, set ny 0, set f 1, set no 0,
eval, output;

set zx 1, set nx 1, set zy 1, set ny 0, set f 1, set no 1,
eval, output;

set zx 0, set nx 0, set zy 1, set ny 1, set f 0, set no 0,
eval, output;

set zx 1, set nx 1, set zy 0, set ny 0, set f 0, set no 0,
eval, output;

set zx 0, set nx 0, set zy 1, set ny 1, set f 0, set no 1,
eval, output;

set zx 1, set nx 1, set zy 0, set ny 0, set f 0, set no 1,
eval, output;

set zx 0, set nx 0, set zy 1, set ny 1, set f 1, set no 1,
eval, output;

set zx 1, set nx 1, set zy 0, set ny 0, set f 1, set no 1,
eval, output;

set zx 0, set nx 1, set zy 1, set ny 1, set f 1, set no 1,
eval, output;

set zx 1, set nx 1, set zy 0, set ny 1, set f 1, set no 1,
eval, output;

set zx 0, set nx 0, set zy 1, set ny 1, set f 1, set no 0,
eval, output;

set zx 1, set nx 1, set zy 0, set ny 0, set f 1, set no 0,
eval, output;

set zx 0, set nx 0, set zy 0, set ny 0, set f 1, set no 0,
eval, output;

set zx 0, set nx 1, set zy 0, set ny 0, set f 1, set no 1,
eval, output;

set zx 0, set nx 0, set zy 0, set ny 1, set f 1, set no 1,
eval, output;

set zx 0, set nx 0, set zy 0, set ny 0, set f 0, set no 0,
eval, output;

set zx 0, set nx 1, set zy 0, set ny 1, set f 0, set no 1,
eval, output;

set zx 1, set nx 1, set zy 1, set ny 1, set f 1, set no 1,
eval, output;

set x %B0000000000000001,
set y %B0000000000000001,

set zx 1, set nx 1, set zy 1, set ny 0, set f 1, set no 0,
eval, output;

set zx 1, set nx 1, set zy 1, set ny 0, set f 1, set no 1,
eval, output;

set zx 0, set nx 0, set zy 1, set ny 1, set f 0, set no 0,
eval, output;

set zx 1, set nx 1, set zy 0, set ny 0, set f 0, set no 0,
eval, output;

set zx 0, set nx 0, set zy 1, set ny 1, set f 0, set no 1,
eval, output;

set zx 1, set nx 1, set zy 0, set ny 0, set f 0, set no 1,
eval, output;

set zx 0, set nx 0, set zy 1, set ny 1, set f 1, set no 1,
eval, output;

set zx 1, set nx 1, set zy 0, set ny 0, set f 1, set no 1,
eval, output;

set zx 0, set nx 1, set zy 1, set ny 1, set f 1, set no 1,
eval, output;

set zx 1, set nx 1, set zy 0, set ny 1, set f 1, set no 1,
eval, output;

set zx 0, set nx 0, set zy 1, set ny 1, set f 1, set no 0,
eval, output;

set zx 1, set nx 1, set zy 0, set ny 0, set f 1, set no 0,
eval, output;

set zx 0, set nx 0, set zy 0, set ny 0, set f 1, set no 0,
eval, output;

set zx 0, set nx 1, set zy 0, set ny 0, set f 1, set no 1,
eval, output;

set zx 0, set nx 0, set zy 0, set ny 1, set f 1, set no 1,
eval, output;

set zx 0, set nx 0, set zy 0, set ny 0, set f 0, set no 0,
eval, output;

set zx 0, set nx 1, set zy 0, set ny 1, set f 0, set no 1,
eval, output;

set zx 1, set nx 1, set zy 1, set ny 1, set f 1, set no 1,
eval, output;

set x %B0000000000010001,
set y %B0000000000000011,

set zx 1, set nx 1, set zy 1, set ny 0, set f 1, set no 0,
eval, output;

set zx 1, set nx 1, set zy 1, set ny 0, set f 1, set no 1,
eval, output;

set zx 0, set nx 0, set zy 1, set ny 1, set f 0, set no 0,
eval, output;

set zx 1, set nx 1, set zy 0, set ny 0, set f 0, set no 0,
eval, output;

set zx 0, set nx 0, set zy 1, set ny 1, set f 0, set no 1,
eval, output;

set zx 1, set nx 1, set zy 0, set ny 0, set f 0, set no 1,
eval, output;

set zx 0, set nx 0, set zy 1, set ny 1, set f 1, set no 1,
eval, output;

set zx 1, set nx 1, set zy 0, set ny 0, set f 1, set no 1,
eval, output;

set zx 0, set nx 1, set zy 1, set ny 1, set f 1, set no 1,
eval, output;

set zx 1, set nx 1, set zy 0, set ny 1, set f 1, set no 1,
eval, output;

set zx 0, set nx 0, set zy 1, set ny 1, set f 1, set no 0,
eval, output;

set zx 1, set nx 1, set zy 0, set ny 0, set f 1, set no 0,
eval, output;

set zx 0, set nx 0, set zy 0, set ny 0, set f 1, set no 0,
eval, output;

set zx 0, set nx 1, set zy 0, set ny 0, set f 1, set no 1,
eval, output;

set zx 0, set nx 0, set zy 0, set ny 1, set f 1, set no 1,
eval, output;

set zx 0, set nx 0, set zy 0, set ny 0, set f 0, set no 0,
eval, output;

set zx 0, set nx 1, set zy 0, set ny 1, set f 0, set no 1,
eval, output;

set zx 1, set nx 1, set zy 1, set ny 1, set f 1, set no 1,
eval, output;

set x %B0111111111111111,
set y %B0000000000000001,

set zx 1, set nx 1, set zy 1, set ny 0, set f 1, set no 0,
eval, output;

set zx 1, set nx 1, set zy 1, set ny 0, set f 1, set no 1,
eval, output;

set zx 0, set nx 0, set zy 1, set ny 1, set f 0, set no 0,
eval, output;

set zx 1, set nx 1, set zy 0, set ny 0, set f 0, set no 0,
eval, output;

set zx 0, set nx 0, set zy 1, set ny 1, set f 0, set no 1,
eval, output;

set zx 1, set nx 1, set zy 0, set ny 0, set f 0, set no 1,
eval, output;

set zx 0, set nx 0, set zy 1, set ny 1, set f 1, set no 1,
eval, output;

set zx 1, set nx 1, set zy 0, set ny 0, set f 1, set no 1,
eval, output;

set zx 0, set nx 1, set zy 1, set ny 1, set f 1, set no 1,
eval, output;

set zx 1, set nx 1, set zy 0, set ny 1, set f 1, set no 1,
eval, output;

set zx 0, set nx 0, set zy 1, set ny 1, set f 1, set no 0,
eval, output;

set zx 1, set nx 1, set zy 0, set ny 0, set f 1, set no 0,
eval, output;

set zx 0, set nx 0, set zy 0, set ny 0, set f 1, set no 0,
eval, output;

set zx 0, set nx 1, set zy 0, set ny 0, set f 1, set no 1,
eval, output;

set zx 0, set nx 0, set zy 0, set ny 1, set f 1, set no 1,
eval, output;

set zx 0, set nx 0, set zy 0, set ny 0, set f 0, set no 0,
eval, output;

set zx 0, set nx 1, set zy 0, set ny 1, set f 0, set no 1,
eval, output;

set zx 1, set nx 1, set zy 1, set ny 1, set f 1, set no 1,
eval, output;

set x %B1000000000000000,
set y %B0000000000000001,

set zx 1, set nx 1, set zy 1, set ny 0, set f 1, set no 0,
eval, output;

set zx 1, set nx 1, set zy 1, set ny 0, set f 1, set no 1,
eval, output;

set zx 0, set nx 0, set zy 1, set ny 1, set f 0, set no 0,
eval, output;

set zx 1, set nx 1, set zy 0, set ny 0, set f 0, set no 0,
eval, output;

set zx 0, set nx 0, set zy 1, set ny 1, set f 0, set no 1,
eval, output;

set zx 1, set nx 1, set zy 0, set ny 0, set f 0, set no 1,
eval, output;

set zx 0, set nx 0, set zy 1, set ny 1, set f 1, set no 1,
eval, output;

set zx 1, set nx 1, set zy 0, set ny 0, set f 1, set no 1,
eval, output;

set zx 0, set nx 1, set zy 1, set ny 1, set f 1, set no 1,
eval, output;

set zx 1, set nx 1, set zy 0, set ny 1, set f 1, set no 1,
eval, output;

set zx 0, set nx 0, set zy 1, set ny 1, set f 1, set no 0,
eval, output;

set zx 1, set nx 1, set zy 0, set ny 0, set f 1, set no 0,
eval, output;

set zx 0, set nx 0, set zy 0, set ny 0, set f 1, set no 0,
eval, output;

set zx 0, set nx 1, set zy 0, set ny 0, set f 1, set no 1,
eval, output;

set zx 0, set nx 0, set zy 0, set ny 1, set f 1, set no 1,
eval, output;

set zx 0, set nx 0, set zy 0, set ny 0, set f 0, set no 0,
eval, output;

set zx 0, set nx 1, set zy 0, set ny 1, set f 0, set no 1,
eval, output;

set zx 1, set nx 1, set zy 1, set ny 1, set f 1, set no 1,
eval, output;

set x %B1111111111111111,
set y %B1111111111111111,

set zx 1, set nx 1, set zy 1, set ny 0, set f 1, set no 0,
eval, output;

set zx 1, set nx 1, set zy 1, set ny 0, set f 1, set no 1,
eval, output;

set zx 0, set nx 0, set zy 1, set ny 1, set f 0, set no 0,
eval, output;

set zx 1, set nx 1, set zy 0, set ny 0, set f 0, set no 0,
eval, output;

set zx 0, set nx 0, set zy 1, set ny 1, set f 0, set no 1,
eval, output;

set zx 1, set nx 1, set zy 0, set ny 0, set f 0, set no 1,
eval, output;

set zx 0, set nx 0, set zy 1, set ny 1, set f 1, set no 1,
eval, output;

set zx 1, set nx 1, set zy 0, set ny 0, set f 1, set no 1,
eval, output;

set zx 0, set nx 1, set zy 1, set ny 1, set f 1, set no 1,
eval, output;

set zx 1, set nx 1, set zy 0, set ny 1, set f 1, set no 1,
eval, output;

set zx 0, set nx 0, set zy 1, set ny 1, set f 1, set no 0,
eval, output;

set zx 1, set nx 1, set zy 0, set ny 0, set f 1, set no 0,
eval, output;

set zx 0, set nx 0, set zy 0, set ny 0, set f 1, set no 0,
eval, output;

set zx 0, set nx 1, set zy 0, set ny 0, set f 1, set no 1,
eval, output;

set zx 0, set nx 0, set zy 0, set ny 1, set f 1, set no 1,
eval, output;

set zx 0, set nx 0, set zy 0, set ny 0, set f 0, set no 0,
eval, output;

set zx 0, set nx 1, set zy 0, set ny 1, set f 0, set no 1,
eval, output;

set zx 1, set nx 1, set zy 1, set ny 1, set f 1, set no 1,
eval, output;

set x %B1111111111111111,
set y %B0000000000000001,

set zx 1, set nx 1, set zy 1, set ny 0, set f 1, set no 0,
eval, output;

set zx 1, set nx 1, set zy 1, set ny 0, set f 1, set no 1,
eval, output;

set zx 0, set nx 0, set zy 1, set ny 1, set f 0, set no 0,
eval, output;

set zx 1, set nx 1, set zy 0, set ny 0, set f 0, set no 0,
eval, output;

set zx 0, set nx 0, set zy 1, set ny 1, set f 0, set no 1,
eval, output;

set zx 1, set nx 1, set zy 0, set ny 0, set f 0, set no 1,
eval, output;

set zx 0, set nx 0, set zy 1, set ny 1, set f 1, set no 1,
eval, output;

set zx 1, set nx 1, set zy 0, set ny 0, set f 1, set no 1,
eval, output;

set zx 0, set nx 1, set zy 1, set ny 1, set f 1, set no 1,
eval, output;

set zx 1, set nx 1, set zy 0, set ny 1, set f 1, set no 1,
eval, output;

set zx 0, set nx 0, set zy 1, set ny 1, set f 1, set no 0,
eval, output;

set zx 1, set nx 1, set zy 0, set ny 0, set f 1, set no 0,
eval, output;

set zx 0, set nx 0, set zy 0, set ny 0, set f 1, set no 0,
eval, output;

set zx 0, set nx 1, set zy 0, set ny 0, set f 1, set no 1,
eval, output;

set zx 0, set nx 0, set zy 0, set ny 1, set f 1, set no 1,
eval, output;

set zx 0, set nx 0, set zy 0, set ny 0, set f 0, set no 0,
eval, output;

set zx 0, set nx 1, set zy 0, set ny 1, set f 0, set no 1,
eval, output;

set zx 1, set nx 1, set zy 1, set ny 1, set f 1, set no 1,
eval, output;

set x %B0001001000110100,
set y %B0101011001111000,

set zx 1, set nx 1, set zy 1, set ny 0, set f 1, set no 0,
eval, output;

set zx 1, set nx 1, set zy 1, set ny 0, set f 1, set no 1,
eval, output;

set zx 0, set nx 0, set zy 1, set ny 1, set f 0, set no 0,
eval, output;

set zx 1, set nx 1, set zy 0, set ny 0, set f 0, set no 0,
eval, output;

set zx 0, set nx 0, set zy 1, set ny 1, set f 0, set no 1,
eval, output;

set zx 1, set nx 1, set zy 0, set ny 0, set f 0, set no 1,
eval, output;

set zx 0, set nx 0, set zy 1, set ny 1, set f 1, set no 1,
eval, output;

set zx 1, set nx 1, set zy 0, set ny 0, set f 1, set no 1,
eval, output;

set zx 0, set nx 1, set zy 1, set ny 1, set f 1, set no 1,
eval, output;

set zx 1, set nx 1, set zy 0, set ny 1, set f 1, set no 1,
eval, output;

set zx 0, set nx 0, set zy 1, set ny 1, set f 1, set no 0,
eval, output;

set zx 1, set nx 1, set zy 0, set ny 0, set f 1, set no 0,
eval, output;

set zx 0, set nx 0, set zy 0, set ny 0, set f 1, set no 0,
eval, output;

set zx 0, set nx 1, set zy 0, set ny 0, set f 1, set no 1,
eval, output;

set zx 0, set nx 0, set zy 0, set ny 1, set f 1, set no 1,
eval, output;

set zx 0, set nx 0, set zy 0, set ny 0, set f 0, set no 0,
eval, output;

set zx 0, set nx 1, set zy 0, set ny 1, set f 0, set no 1,
eval, output;

set zx 1, set nx 1, set zy 1, set ny 1, set f 1, set no 1,
eval, output;

set x %B1000000000000000,
set y %B1000000000000000,

set zx 1, set nx 1, set zy 1, set ny 0, set f 1, set no 0,
eval, output;

set zx 1, set nx 1, set zy 1, set ny 0, set f 1, set no 1,
eval, output;

set zx 0, set nx 0, set zy 1, set ny 1, set f 0, set no 0,
eval, output;

set zx 1, set nx 1, set zy 0, set ny 0, set f 0, set no 0,
eval, output;

set zx 0, set nx 0, set zy 1, set ny 1, set f 0, set no 1,
eval, output;

set zx 1, set nx 1, set zy 0, set ny 0, set f 0, set no 1,
eval, output;

set zx 0, set nx 0, set zy 1, set ny 1, set f 1, set no 1,
eval, output;

set zx 1, set nx 1, set zy 0, set ny 0, set f 1, set no 1,
eval, output;

set zx 0, set nx 1, set zy 1, set ny 1, set f 1, set no 1,
eval, output;

set zx 1, set nx 1, set zy 0, set ny 1, set f 1, set no 1,
eval, output;

set zx 0, set nx 0, set zy 1, set ny 1, set f 1, set no 0,
eval, output;

set zx 1, set nx 1, set zy 0, set ny 0, set f 1, set no 0,
eval, output;

set zx 0, set nx 0, set zy 0, set ny 0, set f 1, set no 0,
eval, output;

set zx 0, set nx 1, set zy 0, set ny 0, set f 1, set no 1,
eval, output;

set zx 0, set nx 0, set zy 0, set ny 1, set f 1, set no 1,
eval, output;

set zx 0, set nx 0, set zy 0, set ny 0, set f 0, set no 0,
eval, output;

set zx 0, set nx 1, set zy 0, set ny 1, set f 0, set no 1,
eval, output;

set zx 1, set nx 1, set zy 1, set ny 1, set f 1, set no 1,
eval, output;

set x %B1010101111001101,
set y %B0001001000110100,

set zx 1, set nx 1, set zy 1, set ny 0, set f 1, set no 0,
eval, output;

set zx 1, set nx 1, set zy 1, set ny 0, set f 1, set no 1,
eval, output;

set zx 0, set nx 0, set zy 1, set ny 1, set f 0, set no 0,
eval, output;

set zx 1, set nx 1, set zy 0, set ny 0, set f 0, set no 0,
eval, output;

set zx 0, set nx 0, set zy 1, set ny 1, set f 0, set no 1,
eval, output;

set zx 1, set nx 1, set zy 0, set ny 0, set f 0, set no 1,
eval, output;

set zx 0, set nx 0, set zy 1, set ny 1, set f 1, set no 1,
eval, output;

set zx 1, set nx 1, set zy 0, set ny 0, set f 1, set no 1,
eval, output;

set zx 0, set nx 1, set zy 1, set ny 1, set f 1, set no 1,
eval, output;

set zx 1, set nx 1, set zy 0, set ny 1, set f 1, set no 1,
eval, output;

set zx 0, set nx 0, set zy 1, set ny 1, set f 1, set no 0,
eval, output;

set zx 1, set nx 1, set zy 0, set ny 0, set f 1, set no 0,
eval, output;

set zx 0, set nx 0, set zy 0, set ny 0, set f 1, set no 0,
eval, output;

set zx 0, set nx 1, set zy 0, set ny 0, set f 1, set no 1,
eval, output;

set zx 0, set nx 0, set zy 0, set ny 1, set f 1, set no 1,
eval, output;

set zx 0, set nx 0, set zy 0, set ny 0, set f 0, set no 0,
eval, output;

set zx 0, set nx 1, set zy 0, set ny 1, set f 0, set no 1,
eval, output;

set zx 1, set nx 1, set zy 1, set ny 1, set f 1, set no 1,
eval, output;
