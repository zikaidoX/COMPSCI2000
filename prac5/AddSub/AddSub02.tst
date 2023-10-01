load AddSub.asm,
output-file AddSub02.out,
compare-to AddSub02.cmp;

set PC 0,
set RAM[0] 0,   // Set R0
set RAM[1] -3,  // Set R1
set RAM[2] -5,  // Set R2
set RAM[3] -1;  // Set R3
repeat 100 {
  ticktock;    // Run for 100 clock cycles
}
set RAM[1] -3,  // Restore arguments in case the program used them
set RAM[2] -5,
set RAM[3] -1,
output;        // Output to file
