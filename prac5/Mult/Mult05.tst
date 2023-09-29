load Mult.asm,
output-file Mult05.out,
compare-to Mult05.cmp,
output-list RAM[0]%D2.6.2 RAM[1]%D2.6.2 RAM[2]%D2.6.2;

set PC 0,
set RAM[0] 0,    // Set R0
set RAM[1] 1,    // Set R1 to 1
set RAM[2] 6;    // Set R2 to a positive integer (6)
repeat 200 {
  ticktock;      // Run for 200 clock cycles
}
set RAM[1] 1,    // Restore arguments in case program used them
set RAM[2] 6,
output;          // Output to file
