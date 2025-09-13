no1 = int(input("Enter first number :"))
no2 = int(input("Enter second number :"))

choice = int(input("1 for Add \n2 for Sub \n3 for Mul \n4 for Div \n\nEnter your choice :- "))

match choice:
    case 1:
        print("Addition = ",no1+no2)
    case 2:
        print("Subtraction = ",no1-no2)
    case 3:
        print("Multiplication = ",no1*no2)
    case 4:
        print("Division = ",no1/no2)
    case _:
        print("Invalid choice")