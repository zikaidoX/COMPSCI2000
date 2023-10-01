// AddSub02.tst
// Test case with negative numbers for AddSub.asm

load AddSub.asm,
output-file AddSub02.out,
compare-to AddSub02.cmp,
output-list RAM[0]%D2.6.2 RAM[1]%D2.6.2 RAM[2]%D2.6.2 RAM[3]%D2.6.2;

set PC 0,
set RAM[0] 0,     // Set R0
set RAM[1] -3,    // Set R1 to a negative number (-3 in this case)
set RAM[2] 2,     // Set R2 to a positive number (2 in this case)
set RAM[3] -1;    // Set R3 to a negative number (-1 in this case)

// Run for 100 clock cycles
repeat 100 {
  ticktock;
}

set RAM[1] -3,    // Restore arguments in case program used them
set RAM[2] 2,
set RAM[3] -1,
output;            // Output to file
