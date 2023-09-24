// Calculates R1 + R2 - R3 and stores the result in R0.
// (R0, R1, R2, R3 refer to RAM[0], RAM[1], RAM[2], and RAM[3], respectively.)

  @R1
  D=M              // D = first number
  @R2
  D=D-M            // D = first number - second number
  @R3
  D=M+D            // D = D +third number
  @R0
  M=D
  @OUTPUT_D         //  Output the Result