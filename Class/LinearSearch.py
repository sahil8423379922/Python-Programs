class search:
  def linearsearch(self,l,t):
    for x in range(len(l)):
      if l[x]==t:
        return x
    else:
      return -1
    
l=[]
for y in range(10):
  n =int(input("Enter a number"))
  l.append(n)

t =int(input("Enter a number to find"))
  
obj = search()
ans =obj.linearsearch(l,t)

if ans ==-1:
  print("Number not found")
else:
  print("Element found at {} position".format(ans))
      
    