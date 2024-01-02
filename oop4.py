class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


point1 = Point(3, 4)
point2 = Point(6, 7)


print(point1.x, point1.y)


class Person:
    def __init__(self, n, a):
        self.name = n
        self.age = a


person1 = Person("Daniel", 24)
person2 = Person("Armando", 57)

print(person1.name)