class ParseException(Exception):
    """
    Raised when tokens provided don't match the expected grammar
    Use this with `raise ParseException("My error message")`
    """
    pass


class ParseTree():

    def __init__(self, node_type, value):
        """
        A node in a Parse Tree data structure
        @param node_type The type of node (see element types).
        @param value The node's value. Should only be used on terminal nodes/leaves, and empty otherwise.
        """
        self.node_type = node_type
        self.value = value
        self.children = []
    

    def addChild(self,child):
        """
        Adds a ParseTree as a child of this ParseTree
        @param child The ParseTree to add
        """
        self.children.append(child)
    

    def getChildren(self):
        """
        Get a list of child nodes in the order they were added.
        @return A LinkedList of ParseTrees
        """
        return self.children
    

    def getType(self):
        """
        Get the type of this ParseTree Node
        @return The type of node (see element types).
        """
        return self.node_type
    

    def getValue(self):
        """
        Get the value of this ParseTree Node
        @return The node's value. Should only be used on terminal nodes/leaves, and empty otherwise.
        """
        return self.value
    

    def __str__(self,depth=0):
        """
        Generate a string from this ParseTree
        @return A printable representation of this ParseTree with indentation
        """        
        # Set indentation
        indent = ""
        for i in range(0,depth):
            indent += "  \u2502 "
        
        # Generate output
        output = ""
        if(len(self.children)>0):
            # Output if the node has children
            output += self.node_type + "\n"
            for child in children:
                output += indent + "  \u2514 " + child.__str__(depth+1)
            
            output += indent + "\n"
        else :
            # Output if the node is a leaf/terminal
            output += self.node_type + " " + self.value + "\n"
        
        return output

    

class Token(ParseTree):

    """
    Token for parsing. Can be used as a terminal node in a ParseTree
    """
    pass
    
