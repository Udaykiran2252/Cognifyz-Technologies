frst = int(input("Enter the first number:"))
scnd =int(input("Enter the second number:"))
op = input("Enter the operator (+,-,*,/,%):")

if op == "+":
    print("Addition of",frst ,"and",scnd ,"is:",frst+scnd)
elif op == "-":
    print("Subtraction of",frst ,"and",scnd ,"is:",frst-scnd)
elif op == "*":
    print("Multiplication of",frst ,"and",scnd ,"is:",frst*scnd)
elif op == "/":
    print("Division of",frst ,"and",scnd ,"is:",frst/scnd)
elif op == "%":
    print("Modulous of",frst ,"and",scnd ,"is:",frst%scnd)
else:
    print("Enter valid operator!")
    
