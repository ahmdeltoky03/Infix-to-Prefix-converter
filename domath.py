def domath(operator,op1,op2=0):# takes operator and operands then returns the result
    
    #the default value is for the special ~ operator
    
    if operator == "+": return op1 + op2

    elif operator == "-": return op1 - op2
    
    elif operator == "%" and op2 != 0: return op1 % op2 # only if no division by zero

    elif operator == "*": return op1 * op2
    
    elif operator == "^": return op1 ** op2

    elif operator == "~": return 0 - op1    #uses 1 operand as u can see

    elif operator == "/" and op2 != 0: return op1 / op2  # only if no division by zero
            
    else :# wrong operators, 0 division
        return "math error"
    
    ## stack.py and validitychecker.py are standard and self explanatory
    ## check the lecture if u want to understand them
    
    ### end of documentation