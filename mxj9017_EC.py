"""
Mehul Jain 1001229017
Lab 3- RPN
OS used: Mac OS Mojave 10.14
Language: Python 3.6
Date: November 14 2018
Assumptions: 1. There are no new line after the last equation in the input txt file.
             2. No brackets in the RPN expression.
             3. Returns values are whole numbers
             4. To run extra credit conversion from algebra to rpn, run the input_EC_RPN.txt
             5. Also added modulus function

"""

def calculator(operator,a,b): # function to return the calculated value
    if (operator=='+'):
        return a+b
    if (operator=='-'):
        return a-b
    if (operator=='*'):
        return a*b
    if (operator=='/'):
        return a//b
    if (operator=='%'):
        return a%b

operators=['+','-','*','/','%'] # modulus function added


def rpn(rpnExpressionList): # get the expression from the file
    valueList = [] # list which will have all the values

    while rpnExpressionList: # while the split list is not empty
        element = rpnExpressionList.pop(0)

        if element in operators: #check if the value is an operator
            b = valueList .pop() #take the second numeric value and pop from the stack
            a = valueList .pop() # take the first numeric value and pop from the stack

            # call the calculator function to calculate the value
            valueList.append(calculator(element,a,b)) # add the calculated value to the stack

        else:
            valueList.append(int(element)) # else just add the read value

    # return the final value which is the first element
    answer= valueList[0]
    return answer


# function to convert algebraic expression to RPN
# working for without brackets
def convertToRPN(algebraicExpression):
    rpnDigits=""
    rpnOperators=""

    for i in algebraicExpression.split():
        if i.isdigit():
            rpnDigits= rpnDigits+" "+i # add the digits to a string
        elif i in operators:
            rpnOperators=i+" "+rpnOperators # add the operators to another string

    rpnExpression=rpnDigits+" "+rpnOperators # concatenate the two string to get the RPN expression
    print("\nAlgebraic Expression:", algebraicExpression)
    print("Alegbraic to RPN conversion: ",rpnExpression)

    rpnExpressionList=rpnExpression.split()
    print("Answer: ",rpn(rpnExpressionList)) # print the answer after converting from alegbraic to RPN



# main function calls

# #for RPN expressions
fileObject = open("input_RPN.txt", "r")
fileRead = fileObject.readlines()

for rpnExpression in fileRead:
    rpnExpressionList=rpnExpression.split()
    print("\nRPN Expression", rpnExpression)
    print("Answer: ",rpn(rpnExpressionList)) # print the answer



print("\n\n******Algebraic to RPN calculation**********")

# for algebraic to RPN Expressions
fileObject = open("input_RPN_EC.txt", "r")
fileRead = fileObject.readlines()

for algebraicExpression in fileRead:
    convertToRPN(algebraicExpression)


