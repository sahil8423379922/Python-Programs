import numpy as np

#Function to take input in list
def takeinput(lt):
  num =int(input("Enter Number"))
  lt.append(num)
  
#Function is to find number and return  
def linearSearch(nu,arr):
  for x in range(len(arr)):
    if nu ==arr[x]:
      return [x,nu]
  return -1
    
  
lt =[]
ch=True

#Loop to call function and ask user to continue or not
while(ch):
  takeinput(lt)
  print("Press Y to continue and Press N to exit")
  i = input()
  if i=='Y' or i=='y':
    ch=True
  elif i=='N' or i=='n':
    ch=False
  else:
    print("Enter Valid Charcter")
    

#Logic to convert list into array
arr =np.array(lt)

#Logic to take input of number that you want to search
nu =int(input("Enter a Number to search in Array ="))

#Logic to Call linear search function
ans= linearSearch(nu,arr)

#Logic to check that element found or not
if ans==-1:
  print("Element not found")
else:
  print("{} is available at {} position".format(ans[1],ans[0]))






    
  
  
