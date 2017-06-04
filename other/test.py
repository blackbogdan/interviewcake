import random

import pprint
import pyautogui, time
# z =  ["{}".format(random.randint(0, 3)) for i in xrange(10)]
# y = "".join(z)
# print "before", z
# random.shuffle(z)
# print z
# m = random.sample(z, len(z))
# print "random sample", m
# m = random.choice("asldfkjsdf")
# print m
# values = [random.randint(1,4) for i in range(1,11)]
# keys = [random.choice("asldfkjsdf") for i in xrange(1,11)]
# print keys, values
# d = zip(keys, values)
# print dict(d)
# print d


# from datetime import datetime
# d = datetime.strptime("19:00:55", "%H:%M:%S")
# print d.minute
# print type(d.hour)
# print d.second

def draw():
    time.sleep(5)
    pyautogui.click()
    distance = 100
    while distance>0:
        pyautogui.dragRel(distance, 0, duration=0.1)
        distance -= 5
        pyautogui.dragRel(0, distance, duration=0.1)
        pyautogui.dragRel(-distance, 0, duration=0.1)
        distance -= 5
        pyautogui.dragRel(0, -distance, duration=0.2)
        # pyautogui.moveTo(1137, 372)
        # pyautogui.dragRel(0, 100, duration=0.1)

# draw()
def drag_n_drop():
    time.sleep(5)
    # pyautogui.click()
    pyautogui.mouseDown(button='left')
    pyautogui.moveRel(0, -300, duration=0.1)
    pyautogui.mouseUp(button='left')

drag_n_drop()

# def scroll_down_100_pixels():
#     pyautogui.scroll(100, 0, 100)
# scroll_down_100_pixels()