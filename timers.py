import time
import inspect
import fieldspace as fsp
from argformater import formatArgs


def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        args_name = inspect.getfullargspec(method)[0]
        functionString = method.__name__ + "(" + formatArgs(args_name,
                                                            args) + ")"
        print("timing- " + fsp.dash_field(functionString, 84), end="\n")

        result = method(*args, **kw)
        te = time.time()
        tc = te - ts
        tcMiliseconds = "{:.2f} ms".format((tc) * 1000)
        if 'log_time' in kw:
            name = kw.get('log_name', method.__name__.upper())
            kw['log_time'][name] = int((te - ts) * 1000)
        else:
            print("timed: ")
            print(fsp.center_equals_field(tcMiliseconds, 92))
            # print("{:.2f} ms".format((te - ts) * 1000))
        return result

    return timed


if __name__ == '__main__':

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
          str(test_time_function(30, [2, 4, 6, 8, 10, 12, 40], None)))