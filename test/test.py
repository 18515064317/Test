from functools import reduce

def calc_prod(lst):
    def lazy_calc_prod():
        def a(x, y):
            return x * y

        return reduce(a, lst)

    return lazy_calc_prod


f = calc_prod([1, 2, 3, 4])
print (f())

def aa():
    print('dsdsd')
    def ab():
        print('abab')
    return ab

def count():
    ff=[]
    for i in range(1,4):
        def fg(j):
            def gg():
                return j*j
            return gg
        r=fg(i)
        ff.append(r)
    return ff
f1,f2,f3=count()
print(f1(),"f2:",f2(),"f3:",f3())


#print (filter(lambda s:s and len(s.strip())>0, ['test', None, '', 'str', '  ', 'END']))

def log(func):
    def wrapper(*args,**kw):
        print('call %s():'%func.__name__)
        return func(*args,**kw)
    return wrapper()
@log
def aa():
    print('sdsfdsf')