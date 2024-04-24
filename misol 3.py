from collections import namedtuple

car = namedtuple('car', ['country', 'model', 'year'])
nexia =['uzbekisatan', 'nexia 2', 2017]
print(car(*nexia))

print(car._make(nexia))