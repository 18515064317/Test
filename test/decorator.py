import functools


def f1(x):
    return x * 2
def new_fn(f):
    def fn(x):
        print('call  '+f.__name__+'()')
        return f(x)
    return fn
g1 = new_fn(f1)
print(g1(5))

import time
from functools import reduce
#
# def performance(f):
#     def usetime(*args,**kw):
#         t1 = time.time()
#         r = f(*args,**kw)
#         t2 = time.time()
#         print('call %s() in %fs' % (f.__name__, (t2 - t1)))
#         return f(*args,**kw)
#     return usetime

def performance1(unit):
    def per_decorator(f):
        def usetime1(*args, **kw):
            t1 = time.time()
            r = f(*args, **kw)
            t2 = time.time()
            if unit == 'ms':
                t = (t2 - t1) * 1000
            else:
                t = (t2 - t1)
            print('call %s() in %f %s' % (f.__name__, t, unit))
            return r
        return usetime1
    return performance1


def performance2(unit):
    def fn(f):
        @functools.wraps(f)
        def wrapper(*args, **kw):
            t1 = time.time()
            r = f(*args, **kw)
            t2 = time.time()
            if unit == 'ms':
                t = (t2 - t1) * 1000
            else:
                t = (t2 - t1)
            print('call %s() in %f %s' % (f.__name__, t, unit))
            return r
        return wrapper
    return fn

def performance(unit):
    def per_decorator(f):
        def wrapper(*args, **kw):
            t1 = time.time()
            r = f(*args, **kw)
            t2 = time.time()
            t = (t2 - t1) * 1000 if unit == 'ms' else (t2 - t1)
            print('call %s() in %f %s' % (f.__name__, t, unit))
            return r

        return wrapper

    return per_decorator

@performance
def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))
print
factorial(10)

class Person(object):

    def __init__(self, name, score):
        self.name = name
        self.__score = score

    def get_grade(self):
        if self.__score >= 80:
            return ('A-优秀')
        if self.__score >= 60 and self.__score < 80:
            return ('B-及格')
        else:
            return ('C-不及格')

p1 = Person('Bob', 90)
p2 = Person('Alice', 65)
p3 = Person('Tim', 48)

print (p1.get_grade())
print (p2.get_grade())
print (p3.get_grade())


def __init__(self, name, score):
    self.__name = name
    self.__score = score


def get_grade(self):
    if self.__score >= 80:
        print
        'A'
    if self.__score >= 60 and self.__score < 80:
        print
        'B'
    else:
        print
        'C'

class Person1(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.get_grade = lambda: 'A'

p3 = Person1('Bob', 90)
print (p3.get_grade)
print (p3.get_grade())


def gcd(a,b):
    if b == 0 :
        return a
    return gcd(b,a%b)
class Rational(object):
    def __init__(self, p, q):
        self.p = p
        self.q = q

    def __add__(self, r):
        return Rational(self.p * r.q + self.q * r.p, self.q * r.q)

    def __sub__(self, r):
        return Rational(self.p * r.q - self.q * r.p, self.q * r.q)

    def __mul__(self, r):
        return Rational(self.p*r.p,self.q*r.q)

    def __truediv__(self, r):
        return Rational(self.p*r.q,self.q*r.p)

    def __str__(self):
        g = gcd(self.q,self.p)
        return '%s/%s'%(self.p / g,self.q / g)

    __repr__ = __str__

r1 = Rational(1, 2)
r2 = Rational(1, 4)
print (r1)
print (r2)
print (r1 + r2)
print (r1 - r2)
print (r1 * r2)
print (r1 / r2)



class Rational2(object):
    def __init__(self, p, q):
        self.p = p
        self.q = q

    def __int__(self):
        return self.p // self.q

    def __float__(self):
        return self.p / self.q

print (float(Rational2(7, 2)))
print (float(Rational2(1, 3)))
print (int(Rational2(7, 2)))
print (int(Rational2(1, 3)))


class Person11(object):

    __slots__ = ('name', 'gender')

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

class Student11(Person11):

    __slots__ = ('name','gander','score')

    def __init__(self,name ,gender , score):
        self.name = name
        self.gender = gender
        self.score = score

s = Student11('Bob', 'male', 59)
s.name = 'Tim'
s.score = 99
print (s.score)
