class code:
  def userdetails(self):
    name =input("Enter the name")
    age =input("Enter the Age")
    return [name,age]
  
    
class vote(code):
  def check(self):
    detail =self.userdetails()
    print(detail)
    
    
class state(vote):
  def employeedetails(self):
    empid =int(input("Enter the Employee ID"))
    print(empid)
    
    
obj =state()
obj.check()
    
  