'''2048.py plays the game 2048 for you and displays your final score.'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Firefox()

browser.get('https://play2048.co/')
game = browser.find_element_by_tag_name('body')

while True:
    gameover = browser.find_elements_by_class_name('game-over')
    if gameover == []:
        for key in (Keys.UP, Keys.RIGHT, Keys.DOWN, Keys.LEFT):
            game.send_keys(key)
    else: break

finalscore = browser.find_elements_by_class_name('best-container')
print('Your score is %s!' % finalscore[0].text)


