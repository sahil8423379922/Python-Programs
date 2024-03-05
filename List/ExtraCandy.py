candies = [2,3,5,1,3]
extraCandies = 3

ans=[]

max =max(candies)
for x in candies:
  if (x+extraCandies)>=max:
    ans.append(True)
  else:
    ans.append(False)
    
print(all(ans))
    

    




