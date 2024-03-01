num =[1,2,3,4,5,6,7,'a',8,9,10]

print("Before Removing Elemet =",num)

#Removing the last element of the list [1,2,3,4,5,6,7,8,9]
num.pop()
print("Removing the last element = ",num)

#Removing the first element [2,3,4,5,6,7,8,9]
num.pop(0)
print("Removing the first element of list =",num)

#Removing element on desired index [2,3,4,5,6,7,8,9]
num.pop(2)
print("Removing from the desired location =",num)

#Removing element by using remove function
num.remove('a')


print(num)

