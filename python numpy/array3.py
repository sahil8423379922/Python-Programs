import numpy


num1 =numpy.array([1,2,3,4,5,6,7,8,9])

print(num1[0])
print(num1[1])

for x in num1:
  print(x)
  
l = len(num1)

print("Length of array =",l)

for x in range(0,l):
  print(num1[x])
  
  
num2 = numpy.array([
  [1,2,3],
  [4,5,6],
  [7,8,9]
])

print(num2[0][0])

l1 =len(num2)
print("Length of matrix = ",l1)

for x in range(l1):
  print("row = ",num2[x])
  for y in num2[x]:
    print("elements = ",y)
  