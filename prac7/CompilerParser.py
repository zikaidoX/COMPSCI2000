from ParseTree import *

class CompilerParser:

    def __init__(self, tokens):
        """
        Constructor for the CompilerParser
        @param tokens A list of tokens to be parsed
        """
        self.tokens = tokens
        self.index = 0

    def compileProgram(self):
        """
        Generates a parse tree for a single program
        @return a ParseTree that represents the program
        """
        if self.have("keyword", "class"):
            return self.compileClass()
        else:
            raise ParseException("Expected 'class' keyword")

    def compileClass(self):
        """
        Generates a parse tree for a single class
        @return a ParseTree that represents a class
        """
        class_tree = ParseTree("class", "")
        self.mustBe("keyword", "class")
        class_tree.addChild(Token("keyword", "class"))

        # Parse class name
        current_tk = self.current()
        if current_tk.getType() == "identifier":
            class_tree.addChild(Token("identifier", current_tk.getValue()))
            self.next()
        else:
            raise ParseException("Expected class name (identifier)")

        self.mustBe("symbol", "{")
        class_tree.addChild(Token("symbol", "{"))

        # Parse class variables and subroutine declarations
        current_tk = self.current()

        # Parse class variable declarations (static and field)
        while current_tk.getValue() in ["static", "field"]:
            if self.have("keyword", "static") or self.have("keyword", "field"):
                class_tree.addChild(self.compileClassVarDec())
                current_tk = self.current()

        # Parse subroutine declarations (constructor, function, method)
        while current_tk.getType() == "keyword":
            if current_tk.getValue() in ["constructor", "function", "method"]:
                class_tree.addChild(self.compileSubroutine())
                current_tk = self.current()

        self.mustBe("symbol", "}")
        class_tree.addChild(Token("symbol", "}"))

        return class_tree
    

    def compileClassVarDec(self):
        """
        Generates a parse tree for a static variable declaration or field declaration
        @return a ParseTree that represents a static variable declaration or field declaration
        """
        class_VarDec = ParseTree("classVarDec", "")
        current_tk = self.current()

        if current_tk.getValue() == "static":
            class_VarDec.addChild(Token("keyword","static"))
        else:
            class_VarDec.addChild(Token("keyword","field"))

        self.next()
        current_tk = self.current()

        if current_tk.getType() == "identifier" or current_tk.getValue() == "int" or current_tk.getValue() == "char" or current_tk.getValue() == "boolean":

            class_VarDec.addChild(Token(current_tk.getType(),current_tk.getValue()))
        else: 
            raise ParseException()
        
        self.next()
        current_tk = self.current()
        
        if current_tk.getType() == "identifier":
            class_VarDec.addChild(Token(current_tk.getType(),current_tk.getValue()))
        else: 
            raise ParseException()
        
        self.next()
        current_tk = self.current()


        while self.have("symbol", ","):
            class_VarDec.addChild((Token("symbol", ",")))
            self.next()
            current_tk = self.current()

            if current_tk.getType() == "identifier":
                class_VarDec.addChild(Token(current_tk.getType(),current_tk.getValue()))
                self.next()
            else:
                raise ParseException()
        
        #self.next()
        current_tk = self.current()
        
        self.mustBe("symbol",";")
        class_VarDec.addChild(Token(current_tk.getType(),current_tk.getValue()))
        

        return class_VarDec
    

    def compileSubroutine(self):
        """
        Generates a parse tree for a method, function, or constructor
        @return a ParseTree that represents the method, function, or constructor
        """
        class_compileSub = ParseTree("subroutine", "")
        current_tk = self.current()

        if current_tk.getType() == "keyword" and current_tk.getValue() == "constructor":
            class_compileSub.addChild(Token("keyword","constructor"))
        elif current_tk.getType() == "keyword" and current_tk.getValue() =="function":
            class_compileSub.addChild(Token("keyword","function"))
        elif current_tk.getType() == "keyword" and current_tk.getValue() == "method":
            class_compileSub.addChild(Token("keyword", "method"))
        else:
            raise ParseException()
        
        self.next()
        current_tk = self.current()

#add type here?
        if current_tk.getType() == "keyword" and current_tk.getValue() == "void":
            class_compileSub.addChild(Token("keyword", "void"))
        elif current_tk.getType() == "keyword" and current_tk.getValue() == "int" or current_tk.getValue() == "char" or current_tk.getValue() == "boolean":
            class_compileSub.addChild(Token("keyword", current_tk.getValue()))
        elif current_tk.getType() == "identifier": 
            class_compileSub.addChild(Token(current_tk.getType(), current_tk.getValue()))
        else:
            raise ParseException()
        
        self.next()
        current_tk = self.current()

# subroutine name? 
        if current_tk.getType() == "identifier":
            class_compileSub.addChild(Token("identifier", current_tk.getValue()))
        else: 
            raise ParseException()
        
# 
        self.next()
        current_tk = self.current()
        #start of parameter list?
        self.mustBe("symbol","(")
        class_compileSub.addChild(Token("symbol",current_tk.getValue()))

        # self.next()
        current_tk = self.current()
# part is getting stuck, is there a missing type here?
        if current_tk.getType() == "keyword" and current_tk.getValue() == "int" or current_tk.getValue() == "char" or current_tk.getValue() == "boolean" or current_tk.getType()=="identifier":
            class_compileSub.addChild(self.compileParameterList())
            current_tk = self.current()

            


        self.mustBe("symbol",")") #symbol breaks here, it's supposed to be a { but only ( works
        class_compileSub.addChild(Token("symbol",")"))
        
        # self.next()
        # current_tk = self.current()

        class_compileSub.addChild(self.compileSubroutineBody())

        return class_compileSub 
    
    
    def compileParameterList(self):
        """
        Generates a parse tree for a subroutine's parameters
        @return a ParseTree that represents a subroutine's parameters
        """
        class_compileParamList = ParseTree("parameterList", "")
        current_tk = self.current()

        if current_tk.getType() == "keyword":
            class_compileParamList.addChild(Token(current_tk.getType(), current_tk.getValue()))
            self.next() 
        elif current_tk.getType() == "identifier":
            class_compileParamList.addChild(Token(current_tk.getType(), current_tk.getValue()))
            self.next() 
        else:
            raise ParseException()
        
        current_tk = self.current()

        if current_tk.getType() == "identifier":
            class_compileParamList.addChild(Token(current_tk.getType(), current_tk.getValue()))
        else:
            raise ParseException()
        
            #self.next() 
            #current_tk = self.current()

        # if len(self.tokens) == 2 and self.index ==1:
        #     pass
        # else:
            self.next() #PROBLEM HERE
        

        while self.have("symbol", ","):
            class_compileParamList.addChild((Token("symbol", ",")))
            #self.next()
            current_tk = self.current()

            if current_tk.getType() == "keyword" and (current_tk.getValue() == "int" or current_tk.getValue() == "char" or current_tk.getValue() == "boolean"):
                class_compileParamList.addChild(Token(current_tk.getType(), current_tk.getValue()))
                self.next()
                #current_tk = self.current()
            elif current_tk.getType() == "identifier":
                class_compileParamList.addChild(Token(current_tk.getType(), current_tk.getValue()))
                self.next()
                #current_tk = self.current()
            # elif current_tk.getType() == "identifier":
            #     class_compileParamList.addChild(Token(current_tk.getType(), current_tk.getValue()))

            else:
                raise ParseException()
            
            current_tk = self.current()
            
            if current_tk.getType() == "identifier":
                 class_compileParamList.addChild(Token("identifier", current_tk.getValue()))
                 self.next()
            elif current_tk.getType() == "symbol":
                class_compileParamList.addChild(Token("symbol", current_tk.getValue()))
                #self.next()
                current_tk = self.current()


        
        return class_compileParamList 
    
    
    def compileSubroutineBody(self):
        """
        Generates a parse tree for a subroutine's body
        @return a ParseTree that represents a subroutine's body
        """
        comp_subroutineBody = ParseTree("subroutineBody", "")
        current_tk = self.current()
#here
            
        self.mustBe("symbol", "{")
        comp_subroutineBody.addChild(Token("symbol", "{"))

        #self.next()
        current_tk = self.current()


        while current_tk.getType() == "keyword" and current_tk.getValue() == "var":
            comp_subroutineBody.addChild(self.compileVarDec())
            current_tk = self.current()
            #self.next()


        while current_tk.getType() == "keyword" and current_tk.getValue() == "let" or current_tk.getValue() == "if" or current_tk.getValue() == "while" or current_tk.getValue() == "do" or current_tk.getValue() == "return":
            comp_subroutineBody(self.compileStatements())
            current_tk = self.current()
            self.next()


        self.mustBe("symbol", "}")
        comp_subroutineBody.addChild(Token("symbol", "}"))



        return comp_subroutineBody 
    
    
    def compileVarDec(self):
        """
        Generates a parse tree for a variable declaration
        @return a ParseTree that represents a var declaration
        """

        comp_vardec = ParseTree("varDec","")
        current_tk = self.current()

        self.mustBe("keyword","var")
        comp_vardec.addChild(Token("keyword","var"))

        
        current_tk = self.current()

        if current_tk.getType() == "keyword" and (current_tk.getValue() == "int" or current_tk.getValue() == "char" or current_tk.getValue() == "boolean"):
            comp_vardec.addChild(Token("keyword", current_tk.getValue()))
        elif current_tk.getType() == "identifier":
            comp_vardec.addChild(Token(current_tk.getType(), current_tk.getValue()))
        else:
            raise ParseException()
        
        self.next()
        current_tk = self.current()

        if current_tk.getType() == "identifier":
            comp_vardec.addChild(Token(current_tk.getType(), current_tk.getValue()))
            self.next() 
            current_tk = self.current()

        while current_tk.getType() == "symbol" and current_tk.getValue() == ",":
            comp_vardec.addChild(Token(current_tk.getType(), current_tk.getValue()))
            self.next()
            current_tk = self.current()

            if current_tk.getType() == "identifier":
                comp_vardec.addChild(Token("identifier", current_tk.getValue()))
                self.next()
                current_tk = self.current()
            else:
                raise ParseException()


        self.mustBe("symbol", ";")
        comp_vardec.addChild(Token("symbol", ";"))

        return comp_vardec 
    

    def compileStatements(self):
        """
        Generates a parse tree for a series of statements
        @return a ParseTree that represents the series of statements
        """

        comp_statements = ParseTree("statements","")
        current_tk = self.current()

        while current_tk.getType() == "keyword" and current_tk.getValue() == "let" or current_tk.getValue() == "if" or current_tk.getValue() == "while" or current_tk.getValue() == "do" or current_tk.getValue() == "return":
            #comp_statements.addChild(Token(current_tk.getType(), current_tk.getValue()))
            current_tk = self.current()
            
            if self.have("keyword", "if"):
                comp_statements.addChild(self.compileIf())
            elif self.have("keyword", "do"):
                comp_statements.addChild(self.compileDo())
            elif self.have("keyword", "let"):
                comp_statements.addChild(self.compileLet())
            elif self.have("keyword", "while"):
                comp_statements.addChild(self.compileWhile())
            elif self.have("keyword", "return"):
                comp_statements.addChild(self.compileReturn())
            else:
                raise ParseException()


        return comp_statements 
    
    
    def compileLet(self):
        """
        Generates a parse tree for a let statement
        @return a ParseTree that represents the statement
        """
        current_tk = self.current()
        compLet = ParseTree("letStatement", "")
        self.mustBe("keyword","let")
        compLet.addChild(Token("keyword","let"))

        current_tk = self.current()


        if current_tk.getType() == "identifier":
            compLet.addChild(Token(current_tk.getType(), current_tk.getValue()))
            self.next() 
            
        else:
            raise ParseException()
#expressions 
        if self.have("symbol","["):
            compLet.addChild(self.compileExpression)
            current_tk = self.current()
            self.next()

            compLet.addChild(Token("symbol","]"))
            self.next()




        current_tk = self.current()

        compLet.addChild(self.mustBe("symbol","="))
        current_tk = self.current()

        if current_tk.getType()=="keyword" and current_tk.getValue()=="skip":
            compLet.addChild(self.compileExpression())
            current_tk = self.current()
        # self.next() 

        if current_tk.getType() == "symbol" and current_tk.getValue() == ";":
            compLet.addChild(Token("symbol",";"))
            self.next()
        else:
            raise ParseException()

        return compLet 


    def compileIf(self):
        """
        Generates a parse tree for an if statement
        @return a ParseTree that represents the statement
        """
        return None 

    
    def compileWhile(self):
        """
        Generates a parse tree for a while statement
        @return a ParseTree that represents the statement
        """
        return None 


    def compileDo(self):
        """
        Generates a parse tree for a do statement
        @return a ParseTree that represents the statement
        """
        compDo = ParseTree("doStatement","")
        current_tk = self.current()
        self.mustBe("keyword","do")
        compDo.addChild(Token("keyword","do"))
        #self.next()

        current_tk = self.current()

        if current_tk.getType()=="keyword" and current_tk.getValue()=="skip":
            compDo.addChild(self.compileExpression())
        else:
            raise ParseException()
        

        current_tk = self.current()
        self.mustBe("symbol",";")

        return compDo 


    def compileReturn(self):
        """
        Generates a parse tree for a return statement
        @return a ParseTree that represents the statement
        """
        comp_Return = ParseTree("returnStatement","")
        current_tk = self.current()
        self.mustBe("keyword","return")

        current_tk = self.current()
        
        if current_tk.getType() == "symbol" and current_tk.getValue() == ";":
            comp_Return.addChild(Token("symbol",";"))
            self.next()
        else:
            raise ParseException()


        return comp_Return 


    def compileExpression(self):
        """
        Generates a parse tree for an expression
        @return a ParseTree that represents the expression
        """
        expression_tree = ParseTree("expression","")
        #expression_tree.addChild("expression","")
        current_tk = self.current()

        if current_tk.getType() == "keyword":
            expression_tree.addChild(Token("keyword","skip"))
            self.next()
        else:
            raise ParseException()

        return expression_tree


    def compileTerm(self):
        """
        Generates a parse tree for an expression term
        @return a ParseTree that represents the expression term
        """
        return None 


    def compileExpressionList(self):
        """
        Generates a parse tree for an expression list
        @return a ParseTree that represents the expression list
        """
        return None 


    def next(self):
        """
        Advance to the next token
        """
        self.index = self.index + 1


    def current(self):
        """
        Return the current token
        @return the token
        """
        if len(self.tokens) > 0:
            return self.tokens[self.index]
        else:
            return None


    def have(self,expectedType,expectedValue):
        """
        Check if the current token matches the expected type and value.
        @return True if a match, False otherwise
        """
        currToken = self.current()

        if currToken == None:
            return False
        
        elif currToken.getType() == expectedType or expectedType == None:
            if currToken.getValue() == expectedValue or expectedValue == None:
                return True
        return False


    def mustBe(self,expectedType,expectedValue):
        """
        Check if the current token matches the expected type and value.
        If so, advance to the next token, returning the current token, otherwise throw/raise a ParseException.
        @return token that was current prior to advancing.
        """
        if self.have(expectedType,expectedValue):
            currToken = self.current()
            self.next()
            return currToken
        else:
            raise ParseException()
        #return None
    

if __name__ == "__main__":


    """ 
    Tokens for:
        class MyClass {
        
        }
    """
    tokens = []


    #parameterlist:
    tokens.append(Token("keyword", "int"))
    tokens.append(Token("identifier", "a"))
    tokens.append(Token("symbol", ","))
    tokens.append(Token("keyword", "char"))
    tokens.append(Token("identifier", "b"))
    tokens.append(Token("symbol", ","))
    tokens.append(Token("keyword", "boolean"))
    tokens.append(Token("identifier", "c"))
    tokens.append(Token("symbol", ","))
    tokens.append(Token("identifier", "Test d"))
    
    parser = CompilerParser(tokens)
    
    try:
        result = parser.compileParameterList()
        #compileClass()
        #compileProgram()
        print(result)
    except ParseException:
        print("Error Parsing!")