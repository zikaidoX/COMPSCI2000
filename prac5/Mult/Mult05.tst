load Mult.asm,
output-file Mult05.out,
compare-to Mult05.cmp,
output-list RAM[0]%D2.6.2 RAM[1]%D2.6.2 RAM[2]%D2.6.2;

set PC 0,
set RAM[0] 0,      // Set R0
set RAM[1] 2147483647,  // Set R1 to a large positive integer (2^31 - 1)
set RAM[2] 3;      // Set R2 to another positive integer (3)
repeat 20000 {
  ticktock;        // Run for 20000 clock cycles
}
set RAM[1] 2147483647,  // Restore arguments in case program used them
set RAM[2] 3,
output;            // Output to file
