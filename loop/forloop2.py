# for i in range(5):
#     print(i) 

# for i in range(1,5+1):
#     # print(i) 
#     print("*",end=" ")

# for i in range(1,6):
#     for j in range(1,6):
#         print("*",end=" ")
#     print("\n")

# num = int(input("Enter the value"))
# for i in range(1,num+1):
#     for j in range(1,num+1):
#         print(j,end=" ")
#     print("\n")

# for i in range(1,6):
#     for j in range(1,6):
#         if i == 1 or j == 1 or i == 5 or j == 5:
#             print("*",end=" ")
#         else: 
#             print(end="  ")
#     print("\n")



# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print("\n")




# for i in range(1,6):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print("\n")


num = int(input("Enter the value"))

for i in range(1,num+1):
    for j in range(1,num+1):
        if i == j or i + j == num+1:
            print("*",end=" ")
        else:
            print(end="  ")
    print("\n")



# num = int(input("Enter the value"))

# for i in range(1,num+1):
#     for j in range(1,num+1):
#         if i == j or i + j == num+1 or i == 1 or j == 1 or i == num or j == num:
#             print("*",end=" ")
#         else:
#             print(end="  ")
#     print("\n")