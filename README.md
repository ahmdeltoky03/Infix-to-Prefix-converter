# Infix_To_Prefix_converter.
An infix expression is expression which is used by us in day today life An infix expression is a single letter, or an operator, proceeded by one infix string and followed by another infix string like A,A + B,(A + B) + (C – D).So,in which we have operators between operands.
An expression is called  prefix expression -->> if the operator appears in the expression before the operands. Simply of the form (operator operand1 operand2).e.g. *+AB-CD
#Conversion from Infix to Prefix expressions.
To convert Infix to Prefix expression, computers usually use the stack data structure.
1. Reverse the infix expression.

2.Obtain the “nearly” postfix expression of the modified expression .

3. Reverse the postfix expression.
