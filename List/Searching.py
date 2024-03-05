#Searching Element in List
a=[]
for x in range(10):
  n=int(input("Enter a number :"))
  a.append(n)
  
num =int(input("Enter the number to find"))

for x in range(len(a)):
  if a[x] == num:
    print("Element found at {} position".format(x))
    break
else:
  print("Element Not Found") 
  
  
  
  