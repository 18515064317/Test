# encoding: utf-8
from types import MethodType

class Student(object):
    def get_score(self):
        return self._score
    def set_score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score=value
s=Student()
s.set_score(70)
print(s.get_score())
s.set_score(99)
print(s.get_score())

class Student1(object):

    @property
    def score1(self):
        return self._score1
    @score1.setter
    def score1(self,value1):
        if not isinstance(value1,int):
            raise ValueError('score must be an integer!')
        if value1 < 0 or value1 > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score1=value1
s1=Student1()
s1.score1=90
print(s1.score1)
s1.score1=70
print(s1.score1)

#@propertyh;;我们在对实例属性操作的时候，就知道该属性很可能不是直接暴露的，而是通过getter和setter方法来实现的。
#还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性：
class Student2(object):
    @property
    def birth(self):
        return 'you birthday is :',self._birth
    @birth.setter
    def birth(self,value):
        self._birth=value
    @property
    def age(self):
        return 'you age is :',2018 - self._birth
b1=Student2()
b1.birth=1992
print(b1.birth)
print(b1.age)

class Screen(object):
    @property
    def width(self):
        return 'width is:',self._width
    @width.setter
    def width(self,value):
        self._width=value
    @property
    def height(self):
        return 'height is :',self._height
    @height.setter
    def height(self,value):
        self._height=value
    @property
    def sum1(self):
        return self._width*2 + self._height*2
    @property
    def resolution(self):
        return self._width*self._height
w1=Screen()
w1.width=8
w1.height=7
print('sum1 is:',w1.sum1)
print('resolution is:',w1.resolution)
if w1.sum1==30:
    print('测试通过!')
else:
    print('测试失败!')
if w1.resolution==56:
    print('测试通过!')
else:
    print('测试失败!')

#多重继承
class Animal(object):
    pass
class Mammal(Animal):
    pass
class Bird(Animal):
    pass
class Dog(Mammal):
    pass
class Bat(Mammal):
    pass
class Parrot(Bird):
    pass
class Ostrich(Bird):
    pass
class Runnable(object):
    def run(self0):
        print('Running ...')
class Flyable(object):
    def fly(self):
        print('Flying')
class Dog(Mammal,Runnable):
    pass
class Bat(Mammal,Flyable):
    pass
#MixIn
#在设计类的继承关系时，通常，主线都是单一继承下来的，例如，Ostrich继承自Bird。但是，如果需要“混入”额外的功能，通过多重继承就可以实现，
# 比如，让Ostrich除了继承自Bird外，再同时继承Runnable。这种设计通常称之为MixIn。


#__init__
class Student4(object):
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return 'Student object (name:%s)'%self.name
print(Student4('msdjkds'))

class Fib(object):
    def __init__(self):
        self.a,self.b=0,1
    def __iter__(self):
        return self
    def __next__(self):
        self.a,self.b=self.b,self.a+self.b
        if self.a>1000:
            raise StopIteration()
        return self.a
for n in Fib():
    print(n)

class Fib2(object):
    def __getitem__(self, h):
        c,d=1,1
        for x in range(h):
            c,d=d,c+d
            return c
f= Fib2()
print(f[200])
print(list(range(100))[2:10])

class Tongji(object):
    def __getitem__(self, i):
        if isinstance(i,int):
            z,v=1,1
            for m in range(i):
                z,v=v,z+v
            return z
        if isinstance(n,slice):
            start=n.start
            stop=n.stop
            if start is None:
                start=0
            z,v=1,1
            L=[]
            for x in range(stop):
                if x >= start:
                    L.append(z)
                z,v=v,z+v
            return L
ff=Tongji()
print(ff[3:9])

class Fib3(object):
    def __getitem__(self, n):
        if isinstance(n, int): # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice): # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L

f5=Fib3()
print(f5[1:5])


class Student5(object):
    def __init__(self,name):
        self.name=name
    def __call__(self):
        print('My name is %s.'%self.name)
stt=Student5('dfgdfg')
print(stt())