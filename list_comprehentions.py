l = [1, 2, 3, 4, 5]

even = [x for x in l if x % 2 == 0]
print(even)

g = lambda x: x**2
print(g(4))
print(dir(l))
class Person():
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return self.name + " " + self.surname

    def get_name(self):
        return self.name
asia = Person('Joanna', 'Koziol')
print(asia)
print(asia.get_name())
print('jshdjsdhjfdshjsfhdhdfhrefhjfdjh\nfdhjfdhjfdhjfdfhjfdhjfdhjdfshjfdshjfdshjfds\nhjdfhdfhjfdhjfdhjdfhjdfhjfdhjfdhjfdhjhjdhjdfhjd')
