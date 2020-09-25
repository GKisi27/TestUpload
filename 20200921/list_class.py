#indexing, slicing, stepping

l1 = [1,2,56,84,22,841,525,44,62,41]
l2 = [9,5,7485,154,8]
# print(l1[0])
# print(l1[1])

#negative indexing
# print(l1[-4])

#Slicing - exclude the last one
# print(l1[0:6])
# print(l1[1:])

# print(l1[0:-5])

#Stepping
# print(l1[::-1])

# l1[1] =20
# print(l1)

# l1.extend(l2)
# # print(l1)
# l3 = l1 +l2
# print(l3)
# t1 = 1,2,5,4
# l4 = list(t1)
# print(l4)


l1 = [1,2,56,84,22,841,525,44,62,41]
# for i,j in enumerate(l1[:5],1):
#     print(f"{i}:{j}")
l2 = [9,5,74,85,154,8]
s = "HelloWorld"

# print(len(l1))
for n in l2:
    l1.append(n)
print(l1)
    

