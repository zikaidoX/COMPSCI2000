load ArrMin.asm,
output-file ArrMin01.out,
compare-to ArrMin01.cmp,
output-list RAM[0]%D2.6.2 RAM[1]%D2.6.2 RAM[2]%D2.6.2 RAM[20]%D2.6.2 RAM[21]%D2.6.2 RAM[22]%D2.6.2 RAM[23]%D2.6.2 RAM[24]%D2.6.2;

set PC 0,
set RAM[0]  0,   // Set R0
set RAM[1]  25,  // Set R1
set RAM[2]  5,   // Set R2
set RAM[20] 7,   // Set Arr[0]
set RAM[21] 0,   // Set Arr[1]
set RAM[22] 4,   // Set Arr[2]
set RAM[23] 6,   // Set Arr[3]
set RAM[24] 9;   // Set Arr[4]
repeat 300 {
  ticktock;    // Run for 300 clock cycles
}
set RAM[1] 25,  // Restore arguments in case program used them
set RAM[2] 5,
output;        // Output to file
