class access:
    public_var = 'this is public variable'
    _protected_var = 'this is protected variable'
    __private_var = 'this is private variable'

    def __init__(self,name):
        self.name = name

obj = access('Ajitesh')
# Printing public variable
print(obj.public_var)

# Printing Protected variable
print(obj._protected_var)

# Printing Private variable
print(obj._access__private_var)
