from collections import namedtuple

market = namedtuple('market', ['name', 'price', 'volume'])

fruit = market('apple', 100, 100)

print(fruit.name)

print(fruit.price)

print(fruit.volume)
