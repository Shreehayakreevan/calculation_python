while True:
    a = int(input("Enter the Number 1 : " ))
    b = int(input("Enter the Number 2 : " ))
    print(a,
          b,)
    sum= a+b
    subtract = a-b
    product = a*b
    divide = a/b
    print("Press 1 to Add")
    print("Press 2 to Subtract")
    print("Press 3 to Product")
    print("Press 4 to Divide")
    operation =(input("Enter the operation you want to do (1,2,3,4): "))
    print(operation)
    if operation == "1":
        print(sum)
    elif operation == "2":
        print(subtract)
    elif operation == "3":
        print(product)
    else:
        print(divide)
    print("Type yes to continue")
    print("Type no to break")
    x = input("Do you Want to Continue or Break : ")
    print(x)
    if x == "yes":
            continue
    else:
            break
    