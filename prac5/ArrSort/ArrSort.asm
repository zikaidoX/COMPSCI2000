// Sorts the array of length R2 whose first element is at RAM[R1] in ascending order in place. Sets R0 to True (-1) when complete.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

@R1      // Load the address of the first element into A
D=M      // Load the value at the first element into D
@ENDLOOP // Label to mark the end of the loop
0;JMP    // Jump to the main loop

LOOP:
    // Compare adjacent elements and swap if necessary
    @R1
    D=M      // Load the value of the current element into D
    @R1+1
    D=D-M    // Compare with the next element

    // If D is positive or zero, the elements are in the correct order, so skip the swap
    D;JGE

    // Swap the elements
    @R1      // Load the address of the first element into A
    D=M      // Load the value at the first element into D
    @R1+1    // Load the address of the second element into A
    M=M-D    // Subtract the value of the first element from the second element
    @R1      // Load the address of the first element into A
    M=M+D    // Add the value of the second element to the first element

ENDLOOP:
    @R1      // Load the address of the first element into A
    D=A      // Load the current address into D
    @R2      // Load the length of the array into A
    D=D-A    // Calculate (RAM address of first element + array length) - current address

    // If D is zero or positive, we have reached the end of the array
    D;JGE

    // Otherwise, continue the loop
    @LOOP
    0;JMP

// Done sorting, set R0 to True (-1)
@R0
M=-1

// Halt the program
@END
0;JMP

(END)