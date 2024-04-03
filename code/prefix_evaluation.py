from stack import stack
from domath import domath

# this function takes a correctly formatted prefix expression, evaluates it,
# then returns the result in case of variables it returns "no result"
# It does that by reversing again and treating the expression as postfix with reversed operand order

def prefixEvaluation(prefixExpr):  # Postfix should have spaces as separators
    
    #create the operand stack and check if infix_to_prefix gave a bracket error 
    opStack = stack()
    tokenList = prefixExpr
    if tokenList == "wrong brackets":return tokenList
    
    tokenList = tokenList.split()[::-1]   #reverse the tokenlist                              
                                                                                                                                                 
                                                                        
    for token in tokenList:# loop over tokens
        
        if token.isdigit() or token.replace(".","").isdigit(): #numbers
            opStack.push(float(token))# add them to operand stack as floats

        elif token=="~":   
        # special negate operator pops only one operand changes its sign then pushs it back                                                     
            operand1 = opStack.pop()
            result = domath(token, operand1)
            opStack.push(result)
            
        elif not token.replace(".","").isalnum(): #operators are not alphanumerics  *(shrugs)
            #pop 2 operands, do operation, push the result
            if opStack.size()<2:return "syntax error" # this is when the user inputs too many operators
            operand1 = opStack.pop()
            operand2 = opStack.pop()
            result = domath(token, operand1, operand2)
            if result =="math error": return result # deals with 0 division, wrong operators and such
            opStack.push(result)                               
        else:
            return "no output"   # when there are letters in the operand                                                
                                                    
    if len(opStack.items) > 1: # this is when the user inputs too many operands
        return "syntax error"           #added this to display to user

    return opStack.pop()# return result

#next file => ./domath.py


#################
# -- Testing -- #
#################

if __name__ == "__main__":
           
    prefix = "* 2 2 "
    print(prefixEvaluation(prefix))
    prefix = "- * 5 6 10 "
    print(prefixEvaluation(prefix))
    prefix = "- * 5 6 10 "
    print(prefixEvaluation(prefix))
    print(prefixEvaluation("****+54321*+21**321"))

