def listsum(a):
  cal=0
  for x in a:
    cal=cal+x
  
  return cal
    

a=[1,2,3,4,5,6,7,8,9,10]
ans =listsum(a)

print("Sum of list  = ",ans)