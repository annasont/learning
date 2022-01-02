'liczby pierwsze'
        
def ifPrimeNumber(y):
    x = y // 2
    if y <= 1:
        return 'Tylko liczby naturalne, większe od jeden mogą być liczbami pierwszymi'
    else:
        while x > 1:
            if y % x == 0:
                return '%d dzieli się przez %d' % (y, x)
                break
            x -= 1
        else:
            return '%d jest liczbą pierwszą' % y


def ifPrimeNumber2(y):
    if y <= 1:
        return 'Tylko liczby naturalne, większe od jeden mogą być liczbami pierwszymi'
    else:
        for x in range(y // 2, 1, -1):
            if y % x == 0:
                return '%d dzieli się przez %d' % (y, x)
                break
            x -= 1
        else:
            return '%d jest liczbą pierwszą' % y

print(ifPrimeNumber(16))
print(ifPrimeNumber2(16))
 
import mytimer

elapsed, result = mytimer.timer(ifPrimeNumber, 17, _reps=100000)
best, result = mytimer.besttime(ifPrimeNumber, 17)
print('First function, total time: %.10f, best time: %.10f, result: %s' % (elapsed, best, result))

elapsed, result = mytimer.timer(ifPrimeNumber2, 17, _reps=100000)
best, result = mytimer.besttime(ifPrimeNumber2, 17)
print('Second function, total time: %.10f, best time: %.10f, result: %s' % (elapsed, best, result))