
# These are the marks of any student for the last three years. You have to calculate total marks for all the three years.

# Sum of the nested list given above - 1142.

marks =[[78, 76, 94, 86, 88],

        [91, 71, 98, 65, 76],

        [95, 45, 78, 52, 49]]

i=0 
sum=0
while i<len(marks):
    j=0
    k=0
    while j<len(marks[i]):
     k=k+marks[i][j]
     j+=1
    sum=sum+k
    i+=1
    print("sum is : ", sum)

# EDGE CASES
marks = [

    [78, 76, 94, 86, 88],

    [91, 71, 98, 65],

    [95, 45, 78]

]
i=0 
sum=0
while i<len(marks):
    j=0
    k=0
    while j<len(marks[i]):
     k=k+marks[i][j]
     j+=1
    sum=sum+k
    i+=1
    print("sum is : ", sum)


marks = [

    [78, 76, 94, 86, 88],

    [91, 71, 98, 65],

    [95, 45, 78],

    [87, 67, 49, 68, 88]

]

i=0 
sum=0
while i<len(marks):
    j=0
    k=0
    while j<len(marks[i]):
     k=k+marks[i][j]
     j+=1
    sum=sum+k
    i+=1
    print("sum is : ", sum)