class student:
  
  def details(self):
    name=input("Enter Name of Student")
    cl =input("Enter the class")
    rollno =input("Enter the rollno")
    self.display(name,cl,rollno)
    
  def display(self,name,cl,rollno):
    print("Name of the student =",name)
    print("Class of the Student =",cl)
    print("Roll no of the student =",rollno)
    

class studentmark(student):
  def mark(self):
    m1 =int(input("Enter Marks of Maths ="))
    m2 =int(input("Enter Marks of English ="))
    m3 =int(input("Enter Marks of Hindi ="))
    m4 =int(input("Enter Marks of GK ="))
    m5 =int(input("Enter Marks of Science ="))
    self.calpercentage(m1,m2,m3,m4,m5)
  
  def calpercentage(self,m1,m2,m3,m4,m5):
    ad=m1+m2+m3+m4+m5
    per =(ad/500)*100
    print("Percentage of Student - {}".format(per))

    
obj =  studentmark()
obj.details()
obj.mark()

    
    