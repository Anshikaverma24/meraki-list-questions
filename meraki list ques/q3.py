# Write a code that prints the maximum in this list.

numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7]
max=numbers[0]
for i in range(0,len(numbers)):
    if (numbers[i]>max):
     max=numbers[i]
     print("maximum number : " , max)