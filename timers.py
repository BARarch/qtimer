#import time
#import inspect
#import fieldspace as fsp
#import timeformater as tf
from . import formats

''' Qtimer special notes:
    LeetCode tester will have two modes speed and debug.  The timer shall be configured to handle both of these modes
    I wonder if I can make a class for the timers

    like this:
    @timer.timeit       ## SPEED: Test all cases for a solution.  Compare speeds across solutions when finnished
        def test (test_solns, cases):
            for test_soln in test_solns:
                for case in cases:
                    test_soln(cases)

    -or
    @timer.timeit      ## DEBUG: Test all solutitions for a case.  Compare results for each case.
        def test (test_solns, cases):
            for case in cases:
                for test_soln in test_solns:    
                    test_soln(cases)

    Timing this will require placeing the @timeit in new locations and composing helpers.
    
    What do I want to time in each scenario?
    For speed it would be each solution finishing all cases
    ...so

    def test (test_solns, cases):

        def compose_test(test_soln):
            @qtimer.timeit_speed
            def speedTest (cases):
                for case in cases:
                    test_soln(case)
        
        

        


        for test_soln in test_solns:
            compose_test(test_soln)


    For debug it would be the time for each case.  
    Output would be minimal...
    def test (test_solns, cases):
            for test_soln in test_solns:
                for case in cases:
                    @qtimer.timeit_debug
                    test_soln(cases)



    I can make compose the tester and move @timeit

    '''


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
    import formats

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