// Multiplies R1 and R2 and stores the result in R0.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Initialize R0 to 0
@0
D=A
@R0
M=D

// Initialize R3 to 0 (used as a counter)
@0
D=A
@R3
M=D

(LOOP)
// R0 = R0 + R1
@R0
D=M
@R1
D=D+M
@R0
M=D

// R3 = R3 + 1
@R3
M=M+1

// Check if R3 = R2
@R3
D=M
@R2
D=D-M
@END
D;JEQ

// If R3 != R2, go back to LOOP
@LOOP
0;JMP

(END)
