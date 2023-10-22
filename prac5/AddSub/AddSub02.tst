load AddSub.asm,
output-file AddSub02.out,
compare-to AddSub02.cmp,
output-list RAM[0]%D2.16.0 RAM[1]%D2.16.0 RAM[2]%D2.16.0 RAM[3]%D2.16.0;

// Set R0 to 0
set RAM[0] 0,

// Set R1 to -3 (in two's complement form: 65536 - 3 = 65533)
set RAM[1] 65533,

// Set R2 to 2 (in two's complement form: 2)
set RAM[2] 2,

// Set R3 to -1 (in two's complement form: 65536 - 1 = 65535)
set RAM[3] 65535;

// Run for 100 clock cycles
repeat 100 {
  ticktock;
}

// Output the final state of RAM
output;
