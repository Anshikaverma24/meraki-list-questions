# Difference

# Q: Given two arrays, 1,2,3,4,5 and 2,3,1,0,5 find which numbers are not present in the second array.

list1 = [1,2,3,4,5,6]

list2 = [2,3,1,0,6,7]

list3=[]
# i=0
# while i<len(list1):
#  if list1[i]!=list2[i]:
#   list1.append(list3)
#   print(list3)
#   i+=1

a=(list1[::])
b=(list2[::])
for i in range(0,len(list1)):
    for j in range(0,len(list2)):
     if a==b:
        print(list1[i])
        # for j in range (0,len(list2)):
     elif b!=a:
        print(list2[i])
