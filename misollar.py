#my_tuple = (1, 2, 3)
#print(my_tuple[0])
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p1 = Point(3, 4)
#print(p1.y)
##print(tuple(namedtuple))

person =('Doston', 25,'doston@gmail.com')

Person1 = namedtuple('Person', ['name', 'age', 'email'])

doston = Person1('Doston', 25, '<doston@gmail.com>')
#print(doston[0])
#doston.name = 'Benazir'
print(Person1)
print(doson)