class Rectangle():
    def __init__(self,length,breadth):
     self.length=length
     self.breadth=breadth
     self.area=self.length*self.breadth
     self.perimeter=2*(self.length+self.breadth)
my=Rectangle(10,20)
my.area
