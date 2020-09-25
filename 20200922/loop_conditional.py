#Condition

a = -30

# if a%5==0 or a%2==0:
#     print("It is divisible by 2 and 5")
# else:
#     print("It is not divisible by 2 and 5")

#Nested if else
# if a%5 == 0:
#     if a%2==0:
#         print("It is divisible by 2 and 5")
#     else:
#         print("It is divisible by 5")
# else:
#     print("It is not divisible by 2 and 5")

if a>0:
    print("a is positive number.")
else:
    print("a is negative number.")

cars = ["maruti","tesla", "mustang","lamborgini"]

new_car = "tesla"
if new_car not in cars:
    cars.append(new_car)
else:
    print("yes, it is in car list.")

print(cars)
    


