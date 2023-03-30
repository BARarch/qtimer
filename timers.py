#import time
#import inspect
#import fieldspace as fsp
#import timeformater as tf
from . import formats


def timeit(method):
    import time
    import inspect

    #from argformater import formatArgs

    def timed(*args, **kw):
        print()
        ts = time.time()
        args_name = inspect.getfullargspec(method)[0]
        functionString = method.__name__ + "(" + formats.formatArgs(
            args_name, args) + ")"
        print(formats.dash_field(functionString, 84), end="\n")

        result = method(*args, **kw)
        te = time.time()
        tc = te - ts
        formatedTime = formats.format_time(tc)
        if 'log_time' in kw:
            name = kw.get('log_name', method.__name__.upper())
            kw['log_time'][name] = int((te - ts) * 1000)
        else:
            print(f"timed: {formatedTime}")
            
        return result

    return timed


if __name__ == '__main__':
    #import formats

    @timeit
    def test_time_function(n, m, p):
        def fibs(m):
            #print("fibs of m = " + str(m))
            if m == 0:
                return m
            elif m == 1:

                return m
            else:
                return fibs(m - 1) + fibs(m - 2)

        return fibs(n)

    print('Result: ' +
          str(test_time_function(31, [2, 4, 6, 8, 10, 12, 40], None)))