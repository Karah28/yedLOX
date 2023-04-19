'''
Задание 1
class Point:
    def def__init__(self, x, y):
        self.x = x
        self.y = y



Задание 2
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x += x
        self.y += y

    def length(self, Point):
        distance = ((self.x - Point.x) ** 2 + (self.y - Point.y) ** 2) ** 0.5
        return round(distance, 2)

Задание 3
class RedButton:
    def __init__(self):
        self.ch = 0

    def click(self):
        print("Тревога!")
        self.ch += 1

    def count(self):
        return self.ch


Задание 4
class Programmer:
    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.worked_hours = 0
        self.salary_per_hour = 0
        self.salary_accumulated = 0
        
        if position == "Junior":
            self.salary_per_hour = 10
        elif position == "Middle":
            self.salary_per_hour = 15
        elif position == "Senior":
            self.salary_per_hour = 20
            
    def work(self, time):
        self.worked_hours += time
        self.salary_accumulated += time * self.salary_per_hour
        
    def rise(self):
        if self.position == "Junior":
            self.salary_per_hour = 15
            self.position = "Middle"
        elif self.position == "Middle":
            self.salary_per_hour = 20
            self.position = "Senior"
        elif self.position == "Senior":
            self.salary_per_hour += 1
            
    def info(self):
        return f"{self.name} {self.worked_hours}ч. {self.salary_accumulated}тгр."

Задание 5
class Rectangle:
    def __init__(self, coordinate1, coordinate2):
        self.x1, self.y1 = coordinate1
        self.x2, self.y2 = coordinate2

    def perimeter(self):
        return round(2 * (abs(self.x2 - self.x1) + abs(self.y2 - self.y1)), 2)

    def area(self):
        return round(abs(self.x2 - self.x1) * abs(self.y2 - self.y1), 2)

Задание 9
class Queue:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop(0)
    
    def is_empty(self):
        return len(self.items) == 0

Задание 10
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

Задание 11
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def length(self, point):
        distance = ((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5
        return round(distance, 2)
        
задание 12

class PatchedPoint(Point):
    def __init__(self, *args):
        if len(args) == 0:
            super().__init__(0, 0)
        elif len(args) == 1:
            super().__init__(args[0][0], args[0][1])
        elif len(args) == 2:
            super().__init__(*args)



class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def length(self, point):
        distance = ((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5
        return round(distance, 2)


class PatchedPoint(Point):
    def __init__(self, *args):
        if len(args) == 0:
            super().__init__(0, 0)
        elif len(args) == 1:
            super().__init__(args[0][0], args[0][1])
        elif len(args) == 2:
            super().__init__(*args)

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"PatchedPoint({self.x}, {self.y})"
Задание 13
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def length(self, point):
        distance = ((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5
        return round(distance, 2)


class PatchedPoint(Point):
    def __init__(self, *args):
        if len(args) == 0:
            super().__init__(0, 0)
        elif len(args) == 1:
            super().__init__(args[0][0], args[0][1])
        elif len(args) == 2:
            super().__init__(*args)

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"PatchedPoint({self.x}, {self.y})"

    def __add__(self, other):
        x, y = other
        return PatchedPoint(self.x + x, self.y + y)

    def __iadd__(self, other):
        x, y = other
        self.move(x, y)
        return self
        
Задание 14
class Fraction:
    def __init__(self, numerator=0, denominator=1):
        if isinstance(numerator, str):
            # если передана строка вида "числитель/знаменатель"
            numerator, denominator = map(int, numerator.split('/'))
        if denominator == 0:
            raise ValueError('Знаменатель не может быть равен нулю')
        # находим общий делитель числителя и знаменателя и делим на него дробь
        common_divisor = self._gcd(numerator, denominator)
        self._numerator = numerator // common_divisor
        self._denominator = denominator // common_divisor

    def numerator(self, number=None):
        if number is not None:
            # если передано новое значение числителя, меняем его
            self._numerator = number
            # сокращаем дробь
            common_divisor = self._gcd(self._numerator, self._denominator)
            self._numerator //= common_divisor
            self._denominator //= common_divisor
        return self._numerator

    def denominator(self, number=None):
        if number is not None:
            # если передано новое значение знаменателя, меняем его
            if number == 0:
                raise ValueError('Знаменатель не может быть равен нулю')
            self._denominator = number
            # сокращаем дробь
            common_divisor = self._gcd(self._numerator, self._denominator)
            self._numerator //= common_divisor
            self._denominator //= common_divisor
        return self._denominator

    def __str__(self):
        return f'{self._numerator}/{self._denominator}'

    def __repr__(self):
        return f'Fraction({self._numerator}, {self._denominator})'

    def _gcd(self, a, b):
        # находим НОД двух чисел
        while b != 0:
            a, b = b, a % b
        return a
        
'''

















































