# Accept a list of numbers from user and

# print a sum of those values
# print minimum value
# print only unique values from those
# print the list of numbers in ascending order
# print the list of numbers in descending order

numList = [1,1,3,2,2,6,5] #hope user input of list need for loop which is not taught, so just assigning
print(sum(numList))
print(min(numList))
print(list(set(numList)))
numList.sort()
print(numList)
numList.sort(reverse=True)
print(numList)

# --Output--
# 20
# 1
# [1, 2, 3, 5, 6]
# [1, 1, 2, 2, 3, 5, 6]
# [6, 5, 3, 2, 2, 1, 1]