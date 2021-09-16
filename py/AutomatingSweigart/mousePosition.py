#! python3
'''mousePosition.py displays the mouse cursor's current position. '''
import pyautogui
print('Press Ctrl-C to quit.')
try:
    while True:
        x, y = pyautogui.position()
        pixelColor = pyautogui.screenshot().getpixel((x, y))
        positionStr = 'X: %4s, Y: %4s, RGB: (%3s, %3s, %3s)' % (x, y, pixelColor[0], pixelColor[1], pixelColor[2])
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    print('\nDone')