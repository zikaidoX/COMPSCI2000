load Mult.asm,
output-file Mult01.out,
compare-to Mult01.cmp,
output-list RAM[0]%D2.6.2 RAM[1]%D2.6.2 RAM[2]%D2.6.2;

set PC 0,
set RAM[0] 0,    // Set R0
set RAM[1] -5,   // Set R1 to a negative integer (-5)
set RAM[2] 3;    // Set R2 to a positive integer (3)
repeat 200 {
  ticktock;      // Run for 200 clock cycles
}
set RAM[1] -5,   // Restore arguments in case program used them
set RAM[2] 3,
output;          // Output to file
