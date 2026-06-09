load Multiplier32.hdl,
output-file Multiplier32.out,
compare-to Multiplier32.cmp,
output-list a%B1.16.1 b%B1.16.1 low%B1.16.1 high%B1.16.1;


set a %B0000000000000000, set b %B0000000000000000, eval, output;
set a %B1111111111111111, set b %B0000000000000000, eval, output;
set a %B0000000000000001, set b %B0000000000000001, eval, output;
set a %B0000000000000010, set b %B0000000000000010, eval, output;