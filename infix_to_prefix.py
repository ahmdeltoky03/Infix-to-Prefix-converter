from stack import stack
from infix_to_prefix_helper import infix_to_prefix_helper

# this file takes an infix expression(string) and converts it to prefix
# it does this by 1-reversing it   2-treating it as a postfix and converting it(with a few adjustments)
# 3-reversing it again 


# this map maps each operator to its precedence in the expression
# the ~ operator in our program is used to indicate a negation operation ex: "-2"=>['~','2'] 
prec = {}
prec["~"] = 5                                                                         
prec["^"] = 4
prec["%"] = 3
prec["*"] = 3
prec["/"] = 3
prec["+"] = 2
prec["-"] = 2
prec[")"] = 1
prec["]"] = 1
prec["}"] = 1

def infix_to_prefix(astring):
    
    # the infex to prefix helper function checks for wrong brackets and filters it 
    # in case of a few edge cases, then it returns a list of (__reversed__) tokens we can use(no spaces)
    tokenlist = infix_to_prefix_helper(str(astring))
    if tokenlist == "wrong brackets": return tokenlist # checks if the helper detected wrong brackets
    
    # create the output(prefix)list and the operator stack
    prefixlist = []
    opstack = stack()

    #loop over every token
    for token in tokenlist:   
        
        
        if  token.replace(".","").isalnum(): # abc | 2003 | .5 | 2.5 |a.2 | .a | 2.a  (operands)
            prefixlist.append(token)         # adds it to output list

        elif token in ")]}":                              
            opstack.push(token)              # notice that the brackets are inverted since 
        # we directly add them to opstack    # we reversed the expression
                                                    
        elif token in "{[(":
            while opstack.peek() not in ")]}":   # we keep poping operands to the output list
                prefixlist.append(opstack.pop()) # until we find the other bracket and pop it
            opstack.pop()
                
        else: #operator
            # we pop anything of higher precedence into the outlist then push the operand to the opstack
            # notice that we dont pop operators of equal precedence since we are iterating backwards
            while not opstack.isempty() and prec[opstack.peek()] > prec[token]:
                prefixlist.append(opstack.pop())
            opstack.push(token)
                                                                
    while not opstack.isempty(): # we pop all remaining operators to the outlist
        prefixlist.append(opstack.pop())
    
    return " ".join(prefixlist[::-1])# we return a reversed prefixlist as a string "+ a b"


# next file => ./infix_to_prefix_helper.py

#################
# -- Testing -- #
#################

if __name__ == "__main__":
    
    print(infix_to_prefix("A + ( C - D ^ 2 ) - { B }")) #True
    print(infix_to_prefix("A + ( C - D ^ 2 } - { B }")) #Different Bracket
    print(infix_to_prefix("(5 * 4 * 3 * 2 * 1) + (2 * 1) + (3 * 2 * 1)")) #NotClosed Bracket
    #print(infix_to_prefix("2 2*3"))