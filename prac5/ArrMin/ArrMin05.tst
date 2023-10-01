load ArrMin.asm,
output-file ArrMin05.out,
compare-to ArrMin05.cmp,
output-list RAM[0]%D2.6.2 RAM[1]%D2.6.2 RAM[2]%D2.6.2;

set PC 0,
set RAM[0]  0,   // Set R0
set RAM[1]  1,   // Set R1
set RAM[2]  1;   // Set R2
repeat 300 {
  ticktock;    // Run for 300 clock cycles
}
set RAM[1] 1,   // Restore arguments in case program used them
set RAM[2] 1,
output;        // Output to file
