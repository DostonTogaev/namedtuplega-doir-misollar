from collections import namedtuple

shakl = namedtuple('Uchburchak', 'nomi turi')

shakl1 = {'nomi':'<uchburchak >', 'turi':'<teng tomonli >'}

print(shakl(**shakl1))

print(shakl1['nomi'])