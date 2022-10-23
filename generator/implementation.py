# iterator
print('demo for iterator')


class A:
    n = 5
    lst = [x for x in range(n)]
    _idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._idx < len(self.lst):
            idx = self._idx
            self._idx += 1
            return self.lst[idx]
        else:
            raise StopIteration


a = A()
a_iter = iter(a)
print('method 1')
for x in a_iter:
    print(x)

# just to reset _idx to go back to the start of the list
print('method 2')
a._idx = 0
for _ in range(3):
    print(next(a_iter))


print('')
# generator
print('demo for generator')


def func(lst):
    idx = 0
    for _ in range(len(lst)):
        yield lst[idx]
        idx += 1


print('method 1')
for x in func([1, 2, 3, 4, 5, 6]):
    print(x)

print('')

g = func([1, 2, 3, 4, 5, 6])
print('method 2')
for _ in range(3):
    print(next(g))
