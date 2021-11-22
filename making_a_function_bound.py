

class Ajitesh:
    
    def method():
        print("this is a method")
        return True


c = Ajitesh()
method = classmethod(Ajitesh.method)
print(Ajitesh.method())