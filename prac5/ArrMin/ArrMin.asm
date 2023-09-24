// Finds the smallest element in the array of length R2 whose first element is at RAM[R1] and stores the result in R0.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Initialize variables
@0     // Set R0 to 0 (initial minimum value)
D=A
@R3
M=D    // Store initial minimum value in R3
@R1    // Load array start address into R1
D=M
@R4
M=D    // Store array start address in R4
@R2    // Load array length into R2
D=M
@R5
M=D    // Store array length in R5
@R4    // Load current element address into R4
D=M
@R6
M=D    // Store current element address in R6

// Loop through array to find minimum value
(LOOP)
    @R5 // Load array length into A register
    D=M
    @END_LOOP
    D;JEQ // If array length is 0, end loop
    @R4 // Load current element address into A register
    D=M
    @R3 // Load minimum value into D register
    D=D-M
    @CHECK_MIN
    D;JGT // If current element is greater than minimum, check next element
    @R4 // Load current element address into R6
    M=D
    @R3 // Store new minimum value in R3
    M=D
(CHECK_MIN)
    @R6 // Load current element address into A register
    D=M
    @1  // Add 1 to current element address to get next element address
    D=D+A
    @R4 // Store next element address in R4
    M=D
    @R5 // Decrement array length
    M=M-1
    @LOOP // Jump to beginning of loop
    0;JMP

// End of loop
(END_LOOP)
    @R3 // Load minimum value into R0 (output)
    D=M
    @R0
    M=D
    @END
    0;JMP
