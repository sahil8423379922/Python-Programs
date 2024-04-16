class code:
  
  def __init__(self,name,empid,bp):
    self.name =name
    self.empid=empid
    self.bp =bp
    self.netsal =None
    self.hra=None
    self.da=None
    self.ta=None
    self.calsal()
    self.printdetail()
    
  def calsal(self):
    self.hra =(self.bp/100)*10
    self.da =(self.bp/100)*5
    self.ta=(self.bp/100)*15
    self.netsal =self.hra +self.da +self.ta +self.bp
    
    
  def printdetail(self):
    print("EMPID of Employee :- ",self.empid)
    print("Name of Employee :- ",self.name)
    print("Basic Pay of Employee :- ",self.bp)
    print("DA of the Employee :- ",self.da)
    print("TA of the Employee :- ",self.ta)
    print("HRA of the Eployee :- ",self.hra)
    print("Net Salary of Employee :- ",self.netsal)
    
    
obj=code('Amit',234,15000)

    