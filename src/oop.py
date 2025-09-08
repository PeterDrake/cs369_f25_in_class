class Student:
    def __init__(self, first, last, id):
        self.first = first
        self.last = last
        self.id = id

s = Student('Bob', 'Dobbs', 13013)
print(s.first)
print(s.last)
print(s.id)

class Tree:
    def __init__(self, height):
        self.height = height

forest = [Tree(100), Tree(80), Tree(107)]
print(forest)

class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return '<' + str(self.x) + ', ' + str(self.y) + '>'

p = Position(3, 5)
print(p)

