// Calculates R1 + R2 - R3 and stores the result in R0.
// (R0, R1, R2, R3 refer to RAM[0], RAM[1], RAM[2], and RAM[3], respectively.)

@R1
D=M             // D = first number (R1)
@R2
D=D-M           // D = first number - second number (R1 - R2)
@R3
D=D+M           // D = D + third number (R1 - R2 + R3)
@R0
M=D             // R0 = R1 - R2 + R3

// Check if R0 is negative and adjust if necessary
@R0
D=M             // D = R0
@NEG_CHECK
D;JLT           // If R0 is negative, jump to NEG_CHECK

@OUTPUT_POSITIVE // Output the Result (for positive integers)
0;JMP

(NEG_CHECK)
@OUTPUT_NEGATIVE // Output the Result (for negative integers)
0;JMP

(OUTPUT_POSITIVE)
@OUTPUT_D        // Output the Result (for positive integers)
0;JMP

(OUTPUT_NEGATIVE)
@OUTPUT_D_NEG    // Output the Result (for negative integers)
0;JMP
