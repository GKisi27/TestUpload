#for loop in list

fruits = ["apple", "banana", "mango", "orange"]

# for fruit in fruits:
#     print(fruit)

# for f in fruits[0]:
#     print(f)

#break
# for fruit in fruits:
#     if fruit == "mango":
#         break
#     else:
#         print(f"{fruit} is not mango.")

#continue
# for fruit in fruits:
#     if fruit == "mango":
#         continue
#     else:
#         print(f"{fruit} is not mango.")

# divisible_by_7 = []
# for i in range(2,101,5):
#     if i%7==0:
#         divisible_by_7.append(i)
# print(divisible_by_7)


#Nested list
numbers = [[1,3,5,7,9],
            [2,4,6,8,10],
            [-12,-15,-95,-75]]
# numbers[0]
#Nested for loop
# for i in numbers:
#     for j in i:
#         print(j)

#Write a Python program to calculate the sum of three given numbers, if the values are equal then return three times of their sum.
a = 15
b = 15
c = 15
s = a+b+c
if a==b==c:
    new_sum = 3*s
    print(new_sum)
else:
    print(s)