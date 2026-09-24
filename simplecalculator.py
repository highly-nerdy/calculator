a = int(input("Enter first number : "))
b = int(input("Enter second number : "))

try:
    i = input("Enter the operation: + , - , * , / : ")
    match i:
        case "+":
            print(f"The sum is {a+b}")
        case "-":
            print(f"The difference is {a-b}")
        case "*":
            print(f"The product is {a*b}")
        case "/":
            if b != 0:
                print(f"The division is {a/b}")
            else:
                print("Division by zero is not possible !")
except Exception as e:
    print(e)