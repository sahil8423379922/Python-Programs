#Taking input of 5 Subject's marks
s1 =int(input("Enter the Marks for Maths : "))
s2 =int(input("Enter the Marks for English : "))
s3 =int(input("Enter the Marks for Hindi : "))
s4 =int(input("Enter the Marks for Computer Science : "))
s5 =int(input("Enter the Marks for Science : "))

#Sum of all subjects
sum = s1 +s2 +s3+ s4+ s5

#Cal Percentage
per =(sum/500)*100
per =round(per,2)

print("Total Marks = {}".format(sum))
print("Total Percentage = {}".format(per))

#Calculating Division
if per<33:
  print("Fail")

elif per<=45:
  print("Third")

elif per<=60:
  print("Second")

elif per>=61 and per<=75:
  print("First")

elif per>=76 and per<=100:
  print("Honours")

else:
  print("Please Enter Valid Marks")





