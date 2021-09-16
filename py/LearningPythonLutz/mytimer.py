"""Funkcja mierząca czas wykonania
Najprostsza wersja:"""

import time
# reps = 1000
# repslistsimple = range(reps)

# def timersimple(func, *pargs, **kargs):
#     start = time.process_time()
#     for i in repslistsimple:
#         ret = func(*pargs, **kargs)
#     elapsed = time.process_time() - start
#     return (elapsed, ret)

timefunc = time.process_time

"Wersja dla pythona 2.6 z wykorzystaniem kargs.pop"

# def timer(func, *pargs, **kargs):
#     _reps = kargs.pop('_reps', 1000)
#     start = timefunc()
#     repslist = range(_reps)
#     for i in repslist:
#         ret = func(*pargs, **kargs)
#     elapsed = timefunc() - start
#     return (elapsed, ret)

# def besttime(func, *pargs, **kargs):
#     _reps = kargs.pop('_reps', 50)
#     repslist = range(_reps)
#     best = 2 ** 32
#     for i in repslist:
#         (time, ret) = timer(func, *pargs, _reps=1, **kargs)
#         if time < best:
#             best = time
#     return (best, ret)


"Funkcja dla pythona 3 z wykorzystaniem argumentu, będącego tylko argumentem kluczowym"

def timer(func, *pargs, _reps=1000, **kargs):
    start = timefunc()
    repslist = range(_reps)
    for i in repslist:
        ret = func(*pargs, **kargs)
    elapsed = timefunc() - start
    return (elapsed, ret)

def besttime(func, *pargs, _reps=50, **kargs):
    repslist = range(_reps)
    best = 2 ** 32
    for i in repslist:
        (time, ret) = timer(func, *pargs, _reps=1, **kargs)
        if time < best:
            best = time
    return (best, ret)
