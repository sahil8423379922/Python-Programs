import numpy as np

#Function to take input in list
def takeinput(lt,lt1):
  num =int(input("Enter 1st Number"))
  num1=int(input("Enter 2nd Number"))
  lt.append(num)
  lt1.append(num1)

#Function is to find number and return  
def linearSearch(nu,arr):
  for x in range(len(arr)):
    for y in range(len(arr[x])):
        if nu ==arr[x][y]:
                    
            return [[x,y],nu]
        
        
  return -1


lt =[]
lt1=[]
ch=True

#Loop to call function and ask user to continue or not
while(ch):
  takeinput(lt,lt1)
  i = input("Press Y to continue and Press N to exit")
  if i=='Y' or i=='y':
    ch=True
  elif i=='N' or i=='n':
    ch=False
  else:
    print("Enter Valid Charcter")


#Logic to convert list into array
arr =np.array([lt,lt1])
#Logic to print the elemenets of both the arrays
# for x in range(len(arr)):
#    for y in range(len(arr[x])):
        

#         print([x,y], "=",arr[x][y])

#Logic to take input of number that you want to search
nu =int(input("Enter a Number to search in Array ="))
# nu1 =int(input("Enter a Number to search in Array2 ="))

print(arr)
#Logic to Call linear search function
ans= linearSearch(nu,arr)


#Logic to check that element found or not
if ans==-1:
  print("Element not found")
else:
  print("{} is available at {} row and {} coloumn in matrix ".format(ans[1],ans[0][0],ans[0][1]))
  
 

  
  
