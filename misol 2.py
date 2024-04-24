from collections import namedtuple

Phone = namedtuple('Phone', 'name  color price')

Iphone = Phone['13 pro max', 'gold', '1000$']

print(Iphone)
print(id(Iphone))
print(hash(Iphone))