// AddSub01.tst
// Test case with negative numbers for AddSub.asm

load AddSub.asm,
output-file AddSub01.out,
compare-to AddSub01.cmp,
output-list RAM[0]%D2.6.2 RAM[1]%D2.6.2 RAM[2]%D2.6.2 RAM[3]%D2.6.2;

set PC 0,
set RAM[0] 0,       // Set R0
set RAM[1] 65533,   // Set R1 to -3 (in two's complement form, 65536 - 3 = 65533)
set RAM[2] 2,       // Set R2 to 2
set RAM[3] 65535;   // Set R3 to -1 (in two's complement form, 65536 - 1 = 65535)

// Run for 100 clock cycles
repeat 100 {
  ticktock;
}

set RAM[1] 65533,   // Restore arguments in case program used them
set RAM[2] 2,
set RAM[3] 65535,
output;              // Output to file
