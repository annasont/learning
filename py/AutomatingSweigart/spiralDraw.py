'''spiralDraw.py draws a spiral drawing. Open paint and after starting program leave the mouse pointer over the paint window.'''
import pyautogui, time
time.sleep(5)
pyautogui.click()

distance = 200
while distance > 0:
    pyautogui.dragRel(distance, 0, duration=0.2)
    distance -= 5
    pyautogui.dragRel(0, distance, duration=0.2)
    pyautogui.dragRel(-distance, 0, duration=0.2)
    distance -= 5
    pyautogui.dragRel(0, -distance, duration=0.2)