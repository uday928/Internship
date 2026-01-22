# List of operations:
ops=['+','-','*','/']

# 1. Operator input
op=input("Enter operator (+ - * /):")

# 1.1 Operator input validation
while(True):
    if op not in ops:
        op=input("Wrong operator!!! Please enter operator(+ - * /) again:")
    else:
        break

# 2. Operands input
a,b=input("Enter first value:"),input("Enter second value:")

# 2.1 Operands input validation
while(True):
    if a.isdigit()==False:
        a=input("Enter first value again:")
        continue
    elif b.isdigit()==False:
        b=input("Enter second value again:")
        continue
    else:
        a=int(a)
        b=int(b)
        break

# 3. Operator wise operations option using match case
match op:
    case '+':
        print("The sum is:",a+b)
    case '-':
        print("The subtraction is:",a-b)
    case '*':
        print("The multiplication is:",a*b)
    case '/':
        # edge case to prevent maths error
        if b!=0:
            print("The division is:",a/b)
        else:
            print("Syntax error(b should not be 0)")
