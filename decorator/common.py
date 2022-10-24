# property
class A:
    def __init__(self):
        self._x = None

    def set_x(self, value):
        print('set x to', value)
        self._x = value

    def get_x(self):
        print('get x')
        return self._x


class B:
    def __init__(self):
        self.x = None

    @property
    def x(self):
        print('get x')
        return self._x

    @x.setter
    def x(self, value):
        print('set x to', value)
        self._x = value


a = A()
a.set_x(1)
print(a.get_x())

b = B()
b.x = 1
print(b.x)

# cache, lru_cache
from functools import cache


# the only difference between cache and lru_cache is lru_cache provide option to limit the cache size
@cache
def two_times(x):
    print('print in side of', two_times.__name__)
    return 2 * x


for _ in range(2):
    print('result of calling two_times is', two_times(2))

# partial
from functools import partial


def sum_of_two(a, b):
    print(f'calling sum_of_two, a={a}, b={b}')
    return a + b


print(sum_of_two(2, 4))

sum_with_2 = partial(sum_of_two, b=2)
print(sum_with_2(3))

# class related decorators: staticmethod, classmethod, abstractclass
