// Multiplies R1 and R2 and stores the result in R0.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Initialize R0 to 0
@0
D=A
@R0
M=D

// Check if R2 is zero, if yes, the result is zero
@R2
D=M
@END
D;JEQ

// Initialize a counter in R3 to keep track of the number of additions
@0
D=A
@R3
M=D

(LOOP)
// Check if R2 is zero, if yes, exit the loop
@R2
D=M
@ENDLOOP
D;JEQ

// Add R1 to R0
@R1
D=M
@R0
M=M+D

// Decrement the counter in R3
@R3
M=M-1

// Jump back to the LOOP label if R3 is not zero
@LOOP
0;JMP

(ENDLOOP)
// End of the loop

(END)
// End of the program
