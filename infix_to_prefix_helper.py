from ValidityChecker import isvalid
import re


# the filter function processes the string to accomodate a few edge cases
# then matches operators and operands then returns them in a list
def filter(astring):
    
    teststring=""
    while teststring!=astring:  #we loop until the regex finds nothing to replace --a -> ~-a -> ~~a
        teststring=astring
        # regular expression
        
        # ~2*3      (~2-3)      2*~3
        # this line replaces all negative numbers & brackets with a special char ~
        astring = re.sub(r"(([^\w\)\]\}\s]|^|\(|\[|\{) *)(\-)",r"\1~",astring)
                   
        #this solves the problem where the user enters +2-1 by removing the '+' (same as up there /\)
        astring = re.sub(r"(([^\w\)\]\}\s]|^|\(|\[|\{) *)(\+)",r"\1",astring)
        
        # this one adds a * between numbers and brackets for this syntax A(B+C)=>A*(B+C)
        astring = re.sub(r"(\w *)(\(|\[|\{)",r"\1*\2",astring)
        
    # this is  a regex that matches words and multi digit numbers 
    # in addition to operators and decimals
    regex=r"\.\w+|\w+(?:\.\w+)?|[^\s\w]"
    
    # here we use the regex to return a list of all matches 
    # while ignoring everything else(spaces,newlines,...etc)
    return re.findall(regex,astring)

def infix_to_prefix_helper(astring):
    '''A function that makes sure that the infix notation is valid and ready to be processed'''
    
    #Handling User Mistakes

        #Incorrectly typed brackets
    if not isvalid(astring):
        print("Brackets are not typed correctly")
        return "wrong brackets"

        
        #Separating Oprators and Operands
    stringlist = filter(astring)

    return stringlist[::-1]




# next file => ./prefix_evalustion.py

#################
# -- Testing -- #
#################

if __name__ == "__main__":
    print(filter("-A2*(5516455231 -3)*( 4%2)-7 ^2"))
