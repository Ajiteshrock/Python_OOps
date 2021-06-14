''' Here let's demonstrate the meaning of decorators'''
def div(a,b):
    print(a/b)

def smart_div(func): #decorator for the function div
    def inner(a,b):
        if(a<b):
            a,b=b,a
        return func(a,b)
    return inner

div = smart_div(div) # This is role of decorators actually you shoul
div(2,4)             #aware of this with the help of decorators we can 
                     #modify a function without touching it