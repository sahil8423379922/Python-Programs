def evenlist(l):
  ans=[]
  for x in l:
    if x%2==0:
      ans.append(x)
      
  return ans

l=[1,2,3,4,5,6,7,8,9,10]
a=evenlist(l)
print("Even List =",a)