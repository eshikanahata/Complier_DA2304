load ,
set sp 256,

set RAM[4000] 1,
set RAM[4001] 2,
set RAM[4002] 1,
set RAM[4003] 2,
set RAM[4004] 1,
set RAM[4005] 2,

set RAM[5000] 1,
set RAM[5001] 1,
set RAM[5002] 1,
set RAM[5003] 1,
set RAM[5004] 1,
set RAM[5005] 1,

set RAM[3000] 1,
set RAM[3001] 1,
set RAM[3002] 1,
set RAM[3003] 1,

repeat 15000 {
    vmstep;
}
output-list RAM[6000]%D2.4.2 RAM[6001]%D2.4.2 RAM[6002]%D2.4.2 RAM[6003]%D2.4.2;
output;