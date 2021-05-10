# Given a list of numbers, output another list that has each number plus it's index. Write a function to achieve this.
# input: [1, 2, 3] output: [1, 3, 5]
# input: [5, 7, 12] output: [5, 8, 14]

numList=[]
count = int(input("Enter the count :"))
print("enter the numbers: ")
for i in range(count):
    numList.append(int(input()))
print("input list : ", numList)
sumList=[]
for index, value in enumerate(numList):
    sumList.append(index+value)

print("Output list : ", sumList)