n1=[1,2,3,4,5]
n2=[1,2,3,4,5,6,7,7]

l =min(len(n1),len(n2))

ans=[]
for x in range(l):
  ans.append((n1[x]+n2[x]))

ans.extend(n2[l:len(n2)])
print(ans)
  