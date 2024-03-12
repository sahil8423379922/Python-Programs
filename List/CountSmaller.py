a=[1,10,9,8,7]
ans=[]
for x in range(0,len(a)):
  count=0
  for y in range(0,len(a)):
    if a[x]>a[y]:
      count=count+1
  ans.append(count)
  
print(ans)
      