# i = 1
# while i <= 10:
#     print(i,end=" ")
#     i = i + 1


# num = 234567
# rev = 0
# while num != 0:
#     rem = num % 10
#     rev = rev * 10 + rem
#     num = num // 10
# print("reverse number ....",rev)


# 345
num = int(input("Enter the number"))
total = 0


while num > 0:
    rem = num % 10
    total = total + rem 
    num = num // 10

print("Sum of digits is ....",total)