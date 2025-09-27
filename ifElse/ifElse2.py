# a = 13
# b = 17

# if a > b:
#     print("A is gretter")
# else:
#     print("B is gretter")




# if a > b and a > c:
#     print("A is gretter")
# elif b > c and b > a:
#     print("B is gretter")
# else:
#     print("C is gretter")
# a = 25
# b = 22
# c = 30

# if a > b:
#     if a > c:
#         print("A is gretter")
#     else:
#         print("C is gretter")
# else:
#     if b > c:
#         print("B is gretter")
#     else:
#         print("C is gretter")


# amount  : 4897 

# 500 - 9 
# 200 - 1 
# 100 - 1
# 50 - 1
# 20 - 2 
# 10  - 0 
# 5 - 1 
# 2 - 1 
# 1 - 0  


# a = 10
# # print(type(a))
# print(type(a) == list)


# no1 = int(input("Enter first number: "))
# no2 = int(input("Enter second number: "))

# if no1 > no2:
#     print("First number is greater")
# else:
#     print("Second number is greater")


# num = int(input("Enter a number:"))

# if num % 2 == 0:
#     print("Even number")
# else:
#     print("Odd number")

# no1 = int(input("Enter first number: "))
# no2 = int(input("Enter second number: "))
# no3 = int(input("Enter third number: "))

# sum = 0

# if no1 > 60:
#     sum += no1 
# if no2 > 60:
#     sum += no2
# if no3 > 60:
#     sum += no3

# print(sum)


# no1 = int(input("Enter first number: "))
# no2 = int(input("Enter second number: "))
# no3 = int(input("Enter third number: "))


# with logical operators
# if no1 > no2 and no1 > no3:
#     print("First number is greater")
# elif no2 > no1 and no2 > no3:
#     print("Second number is greater")
# else:
#     print("Third number is greater")


# without logical operators

# if no1 > no2:
#     if no1 > no3:
#         print("First number is greater")
#     else:
#         print("Third number is greater")
# else:
#     if no2 > no3:
#         print("Second number is greater")
#     else:
#         print("Third number is greater")


# 90 

# eng = int(input("Enter number of engineers: "))
# math = int(input("Enter number of mathematicians: "))
# science = int(input("Enter number of scientists: "))
# bio = int(input("Enter number of biologists: "))


# total = eng + math + science + bio

# percentage =  (total / 400) * 100

# if percentage > 90:
#     grade = "A"
# elif percentage > 80:
#     grade = "B"
# elif percentage > 70:
#     grade = "C"
# elif percentage > 60:
#     grade = "D"
# elif percentage > 50:
#     grade = "E"
# else:
#     grade = "F"

# print(f"Total marks of all subject : {total}")
# print(f"Percentage of all subject : {percentage}%")
# print(f"Grade is : {grade}")


month = int(input("Enter month number: "))

if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    print("31 days")
elif month == 2:
    print("28 days")
else:
    print("30 days")