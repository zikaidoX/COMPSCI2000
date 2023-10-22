load Mult.asm,
output-file Mult04.out,
compare-to Mult04.cmp,
output-list RAM[0]%D2.6.2 RAM[1]%D2.6.2 RAM[2]%D2.6.2;

set PC 0,
set RAM[0] 0,    // Set R0
set RAM[1] 0,    // Set R1 to 0
set RAM[2] 8;    // Set R2 to a positive integer (8)
repeat 200 {
  ticktock;      // Run for 200 clock cycles
}
set RAM[1] 0,    // Restore arguments in case program used them
set RAM[2] 8,
output;          // Output to file
