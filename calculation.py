while True:
#Getting input from the user
    a = int(input("Enter the Number 1 : " ))
    b = int(input("Enter the Number 2 : " ))
    print(a,
          b,)
    sum= a+b
    subtract = a-b
    product = a*b
    divide = a/b
#Giving choices inorder to make my program user friendly
    print("Press 1 to Add")
    print("Press 2 to Subtract")
    print("Press 3 to Product")
    print("Press 4 to Divide")
#asking the function which is required
    operation =(input("Enter the operation you want to do (1,2,3,4): "))
    print(operation)
#Getting the operation required
    if operation == "1":
        print("Sum of two numbers =" ,sum)
    elif operation == "2":
        print("Subtraction of two numbers =" ,subtract)
    elif operation == "3":
        print("Product of two numbers =" ,product)
    else:
        print("Division of two numbers =" ,divide)
#whether to continue or break
    print("Type yes to continue")
    print("Type no to break")
    x = input("Do you Want to Continue or Break : ")
    print(x)
    if x == "yes":
            continue
    else:
            break
