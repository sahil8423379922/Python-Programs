import math
class code:
  
  def sqrt(self,l):
    sq=[]
    for x in l:
      a =math.sqrt(x)
      sq.append(a)
      
    return sq
  

l =[]

for x in range(10):
  num =int(input("Enter a number :- "))
  l.append(num)
  
obj =code()
ans=obj.sqrt(l)

print("List of sqare root =",ans)