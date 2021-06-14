class outer:
    def __init__(self):
        self.name = "Ajitesh Mishra"
        self.ine = self.inner()

    def Aj(self):
        print("This is outer class and your name is ",self.name)

    class inner:

        def __init__(self):
            self.car="Mercedes Benz"

        def Mish(self):
            print("This is inner class and your car is", self.car)


o = outer()
o.Aj()

a=outer.inner() ##creating object of inner class
b = o.ine #sencond method to create object of inner class
print("calling inner class' method")
print(a.car,b.Mish()) #function will be called first because of comma operator
