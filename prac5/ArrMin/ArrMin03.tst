load ArrMin.asm,
output-file ArrMin03.out,
compare-to ArrMin03.cmp,
output-list RAM[0]%D2.6.2 RAM[1]%D2.6.2 RAM[2]%D2.6.2 RAM[20]%D2.6.2 RAM[21]%D2.6.2 RAM[22]%D2.6.2 RAM[23]%D2.6.2;

set PC 0,
set RAM[0]  0,   // Set R0
set RAM[1]  10,  // Set R1
set RAM[2]  5,   // Set R2
set RAM[20] -2,  // Set Arr[0]
set RAM[21] 4,   // Set Arr[1]
set RAM[22] 0,   // Set Arr[2]
set RAM[23] 8;   // Set Arr[3]
repeat 300 {
  ticktock;    // Run for 300 clock cycles
}
set RAM[1] 10,  // Restore arguments in case program used them
set RAM[2] 5,
output;        // Output to file