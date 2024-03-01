#Creating a list
num=[]

for x in range(10):
  n =int(input("Enter the number at {} position = ".format(x)))
  
  #Inserting Element in the list
  num.append(n)

print(num)

#Sum of elements in list
print(sum(num))