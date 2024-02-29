// Test case for AddSub.vm
// Tests AddSub.vm with negative input values

load AddSub.vm,
output-file AddSub01.out,
compare-to AddSub01.cmp,
output-list sp%D1.6.1 local%D1.6.1 argument%D1.8.1 this%D1.6.1 that%D1.6.1
            RAM[16]%D1.6.1 RAM[17]%D1.6.1 RAM[18]%D1.6.1
            local[0]%D1.8.1 local[1]%D1.8.1 local[2]%D1.8.1
            argument[0]%D1.11.1 argument[1]%D1.11.1 argument[2]%D1.11.1;

set sp 256,        // stack pointer
set local 300,     // base address of the local segment
set argument 400,  // base address of the argument segment
set this 3000,     // base address of the this segment
set that 3010,     // base address of the that segment

set RAM[16] -5,  // static 0 (negative value)
set RAM[17] -8,  // static 1
set RAM[18] 3,   // static 2

set local[0] -15,  // local 0 (negative value)
set local[1] -25,  // local 1 (negative value)
set local[2] -35,  // local 2 (negative value)

set argument[0] 150,  // argument 0
set argument[1] 250,  // argument 1
set argument[2] 350;  // argument 2

repeat 25 {        // Change this number to cover the number of instructions in the VM test file
  vmstep;
}
output;
