// Calculates the absolute value of R1 and stores the result in R0.
// (R0, R1 refer to RAM[0], and RAM[1], respectively.)

// load R1 into D
@R1
D=M

// check if D is negative
@NEG
D;JLT

// if D is positive or zero, set R0 to D
@R0
M=D
@END
0;JMP

// if D is negative, negate it and set R0 to the result
(NEG)
D=-D
@R0
M=D

(END)
// End of program
