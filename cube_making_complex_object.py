class Sqaure:
    def __init__(self,side):
        print("parent constructor running")
        self.side = side
    
    def area(self):
        return self.side ** 2

class Cube:

    def __new__(cls):
        print("object created")
        cls.__init_(cls)
        
    def __init_(self):
        print("child constructor running")
    
    def surface_area(self):
        return 6 * 23


s=Cube()
# so __init__ is not the constructor