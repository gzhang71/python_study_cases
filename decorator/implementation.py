from functools import wraps


def funcname_not_wrapped(func):
    def wrapper(*args, **kwargs):
        print('calling function', func.__name__)
        res = func(*args, **kwargs)
        return res

    return wrapper


def funcname_wrapped(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('calling function', func.__name__)
        res = func(*args, **kwargs)
        return res

    return wrapper


@funcname_not_wrapped
def f1():
    print('hello world!')


@funcname_wrapped
def f2():
    print('hello world!')


def f():
    print('hello world!')


f3 = funcname_not_wrapped(f)

f4 = funcname_wrapped(f)

if __name__ == '__main__':
    for x in [f1, f2, f3, f4]:
        x()
        print(x.__name__)
        print('')

