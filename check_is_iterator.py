def iterable(value):
    try:
        iter(value)
        return True
    except TypeError:
        return False

print(iterable([1,3,4,4]),
iterable({"2":3}), 
iterable('33423423'),
iterable(1))

