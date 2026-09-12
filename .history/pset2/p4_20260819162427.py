n1 = int (input("Enter first number"))
n2 = int (input("Enter second number"))

operation = input("Choose operations")
match operation:
    case "1":
        print(n1+n2)

    case 2:
        print(n1-n2)

    case 3:
        print(n1 * n2)
     