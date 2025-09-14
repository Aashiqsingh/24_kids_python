# no1 = int(input("Enter a number :"))

# match no1%2 == 0:
#     case True:
#         print("Even")
#     case False:
#         print("Odd")


no1 = 14
no2 = 13
no3 = 15
# ans = "no1 is gretter" if no1 > no2 else "no2 is greater"


ans = "no1 is gretter" if no1 > no2 and no1 > no3 else "no2 is grettre" if no2 > no3 else "no3 is gretter"
print(ans)