class VMTranslator:

    # Initialize a label counter for unique label generation
    label_counter = 0
    
    @staticmethod
    def vm_push(segment, offset):
        asm_code = ""
        if segment == "constant":
            asm_code = f"// push {segment} {offset}\n"
            asm_code += f"@{offset}\nD=A\n@SP\nA=M\nM=D\n@SP\nM=M+1\n"
        # Add more cases for other memory segments (local, argument, this, that, temp, static, pointer)
        return asm_code

    @staticmethod
    def vm_pop(segment, offset):
        asm_code = ""
        if segment == "static":
            asm_code = f"// pop {segment} {offset}\n"
            asm_code += f"@SP\nM=M-1\nA=M\nD=M\n@{segment}.{offset}\nM=D\n"
        # Add more cases for other memory segments (local, argument, this, that, temp, pointer)
        return asm_code

    @staticmethod
    def vm_add():
        asm_code = "// add\n"
        asm_code += "@SP\nM=M-1\nA=M\nD=M\nA=A-1\nM=M+D\n"
        return asm_code

    @staticmethod
    def vm_eq():
        asm_code = "// eq\n"
        eq_label = f"EQ_LABEL_{VMTranslator.label_counter}"
        VMTranslator.label_counter += 1
        asm_code += "@SP\nM=M-1\nA=M\nD=M\nA=A-1\nD=M-D\n"
        asm_code += f"@{eq_label}_TRUE\nD;JEQ\n"
        asm_code += f"@{eq_label}_FALSE\n0;JMP\n"
        asm_code += f"({eq_label}_TRUE)\n@SP\nA=M-1\nM=-1\n"
        asm_code += f"@{eq_label}_END\n0;JMP\n"
        asm_code += f"({eq_label}_FALSE)\n@SP\nA=M-1\nM=0\n"
        asm_code += f"({eq_label}_END)\n"
        return asm_code

    @staticmethod
    def vm_gt():
        asm_code = "// gt\n"
        gt_label = f"GT_LABEL_{VMTranslator.label_counter}"
        VMTranslator.label_counter += 1
        asm_code += "@SP\nM=M-1\nA=M\nD=M\nA=A-1\nD=M-D\n"
        asm_code += f"@{gt_label}_TRUE\nD;JGT\n"
        asm_code += f"@{gt_label}_FALSE\n0;JMP\n"
        asm_code += f"({gt_label}_TRUE)\n@SP\nA=M-1\nM=-1\n"
        asm_code += f"@{gt_label}_END\n0;JMP\n"
        asm_code += f"({gt_label}_FALSE)\n@SP\nA=M-1\nM=0\n"
        asm_code += f"({gt_label}_END)\n"
        return asm_code

    @staticmethod
    def vm_label(label):
        asm_code = f"({label})\n"
        return asm_code

    @staticmethod
    def vm_goto(label):
        asm_code = f"// goto {label}\n"
        asm_code += f"@{label}\n0;JMP\n"
        return asm_code

    @staticmethod
    def vm_if(label):
        asm_code = f"// if-goto {label}\n"
        asm_code += "@SP\nM=M-1\nA=M\nD=M\n"
        asm_code += f"@{label}\nD;JNE\n"
        return asm_code

    @staticmethod
    def vm_function(function_name, n_vars):
        asm_code = f"// function {function_name} {n_vars}\n"
        asm_code += f"({function_name})\n"
        for _ in range(n_vars):
            asm_code += VMTranslator.vm_push("constant", 0)
        return asm_code

    @staticmethod
    def vm_call(function_name, n_args):
        asm_code = f"// call {function_name} {n_args}\n"
        return_label = f"RETURN_LABEL_{VMTranslator.label_counter}"
        VMTranslator.label_counter += 1
        asm_code += f"@{return_label}\nD=A\n@SP\nA=M\nM=D\n@SP\nM=M+1\n"
        asm_code += VMTranslator.vm_push("local", 0)
        asm_code += VMTranslator.vm_push("argument", 0)
        asm_code += VMTranslator.vm_push("this", 0)
        asm_code += VMTranslator.vm_push("that", 0)
        # Adjust ARG and LCL for the new function call
        asm_code += "@SP\nD=M\n@{n_args + 5}\nD=D-A\n@ARG\nM=D\n"
        asm_code += "@SP\nD=M\n@LCL\nM=D\n"
        asm_code += VMTranslator.vm_goto(function_name)
        asm_code += f"({return_label})\n"
        return asm_code

    @staticmethod
    def vm_return():
        asm_code = "// return\n"
        asm_code += "@LCL\nD=M\n@R13\nM=D\n"  # R13 holds the frame
        asm_code += "@5\nA=D-A\nD=M\n@R14\nM=D\n"  # R14 holds the return address
        asm_code += VMTranslator.vm_pop("argument", 0)
        asm_code += "@ARG\nD=M\n@SP\nM=D+1\n"  # Restore SP
        asm_code += "@R13\nA=M-1\nD=M\n@THAT\nM=D\n"
        asm_code += "@R13\nA=M-1\nA=A-1\nD=M\n@THIS\nM=D\n"
        asm_code += "@R13\nA=M-1\nA=A-1\nA=A-1\nD=M\n@ARG\nM=D\n"
        asm_code += "@R13\nA=M-1\nA=A-1\nA=A-1\nA=A-1\nD=M\n@LCL\nM=D\n"
        asm_code += "@R14\nA=M\n0;JMP\n"  # Jump to the return address
        return asm_code


# A quick-and-dirty parser when run as a standalone script.
if __name__ == "__main__":
    import sys
    if(len(sys.argv) > 1):
        with open(sys.argv[1], "r") as a_file:
            for line in a_file:
                tokens = line.strip().lower().split()
                if(len(tokens)==1):
                    if(tokens[0]=='add'):
                        print(VMTranslator.vm_add())
                    elif(tokens[0]=='sub'):
                        print(VMTranslator.vm_sub())
                    elif(tokens[0]=='neg'):
                        print(VMTranslator.vm_neg())
                    elif(tokens[0]=='eq'):
                        print(VMTranslator.vm_eq())
                    elif(tokens[0]=='gt'):
                        print(VMTranslator.vm_gt())
                    elif(tokens[0]=='lt'):
                        print(VMTranslator.vm_lt())
                    elif(tokens[0]=='and'):
                        print(VMTranslator.vm_and())
                    elif(tokens[0]=='or'):
                        print(VMTranslator.vm_or())
                    elif(tokens[0]=='not'):
                        print(VMTranslator.vm_not())
                    elif(tokens[0]=='return'):
                        print(VMTranslator.vm_return())
                elif(len(tokens)==2):
                    if(tokens[0]=='label'):
                        print(VMTranslator.vm_label(tokens[1]))
                    elif(tokens[0]=='goto'):
                        print(VMTranslator.vm_goto(tokens[1]))
                    elif(tokens[0]=='if-goto'):
                        print(VMTranslator.vm_if(tokens[1]))
                elif(len(tokens)==3):
                    if(tokens[0]=='push'):
                        print(VMTranslator.vm_push(tokens[1],int(tokens[2])))
                    elif(tokens[0]=='pop'):
                        print(VMTranslator.vm_pop(tokens[1],int(tokens[2])))
                    elif(tokens[0]=='function'):
                        print(VMTranslator.vm_function(tokens[1],int(tokens[2])))
                    elif(tokens[0]=='call'):
                        print(VMTranslator.vm_call(tokens[1],int(tokens[2])))

        