print("Welcome to the hotel menu!")

print("\n1 for Gujart")
print("2 for Punjabi")
print("3 for Chinese")
print("4 for Indian")
print("5 for Marwadi")

choice = int(input("\nEnter your choice :"))
match choice:
    case 1:
        print("You selected Gujarati dish.")
        print("1 for Dhokla")
        print("2 for sev tamata")
        print("3 for Khaman")

        gujaratiChoice = int(input("\nEnter your choice :"))
        match gujaratiChoice:
            case 1: 
                plates = int(input("\n How many plates you want :"))
                print("Your total amount will be", plates*50)

            case 2:
                plates = int(input("\n How many plates you want :"))
                print("Your total amount will be", plates*60)
            
            case 3:
                plates = int(input("\n How many plates you want :"))
                print("Your total amount will be", plates*70)
    case 2:
        print("You selected Punjabi dish.")
        print("1 for paneer tikka")
        print("2 for cheese butter masala")
        print("3 for sarso da saag")
    case 3:
        print("You selected Chinese dish.")
        print("1 for soup")
        print("2 for rice")
        print("3 for curry")
    case 4:
        print("You selected Indian dish.")
        print("1 for samosa")
        print("2 for paneer tikka")
        print("3 for masala")
    case 5:
        print("You selected Marwadi dish.")
        print("1 for samosa")
        print("2 for paneer tikka")
        print("3 for masala")
