'''stopwatch.py'''
import time
print('Press enter to begin. Afterwards, press enter to "click" the stopwatch. Press Ctrl-C to quit.')
input()
print('Started')

startTime = time.time()
lastTime = startTime
lapNum = 1

try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        print('Lap %3s: %5s (Total time: %7s)' % (lapNum, lapTime, totalTime))
        lapNum += 1
        lastTime = time.time()

except:
    print('Done!')



