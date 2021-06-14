# list of cities
cities = ["Berlin", "Vienna", "Zurich"]


iterator_obj = iter(cities)  # here cities is iterbale and iterator_obj is the
# object of that iterator we call the next method for iterating over all the elements
# of the list itself
print(next(iterator_obj))
print(next(iterator_obj))
print(next(iterator_obj))
