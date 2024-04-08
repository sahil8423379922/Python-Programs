class code:
  
  def gcd(self,l):
    num=0
    for x in l:
      count=0
      
      for y in l:
        if y%x==0:
          count =count+1
     
      
      if count ==len(l):
        
        if x>num:
          num=x

          
        
        
    return num
  
  

l=[6,9,18]
obj =code()
ans = obj.gcd(l)

if ans==0:
  print("GCD of list is = 1")
else:
  print("GCD of List is = ",ans)

