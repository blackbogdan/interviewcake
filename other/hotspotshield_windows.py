__author__ = 'bkapusta'
from PIL import Image, ImageDraw, ImageGrab
# pip install pillow
import time
from ctypes import windll
import subprocess
import pyautogui
import requests
# took the code from:
# https://stackoverflow.com/questions/21338431/finding-the-position-of-an-object-in-an-image
def start_hotspot_shield_app():
    path_to_the_app = 'C:\\Program Files (x86)\\Hotspot Shield\\bin\\hsscp.exe'
    subprocess.call([path_to_the_app])


def take_screenshot(filename="screenshot_taken_with_python.jpg"):
    '''
    takes screenshot of the window and saves it in to current directory.
    Takes input as a file name
    '''
    # this is a workaround that makes python to take screenshot of whole screen
    user32 = windll.user32
    user32.SetProcessDPIAware()
    # end of workaround
    img = ImageGrab.grab()
    img.save(filename)

def find_button_position():
    # opening images
    d_im = Image.open("discon_icon.png")
    sb_im = Image.open("before_vpn.png")
    d_im_size = d_im.size
    sb_im_size = sb_im.size
    # print d_im_size
    # print sb_im_size

    # getting middle pixel of an image:
    x0, y0 = d_im_size[0]//2, d_im_size[1]//2
    # this will return tuple: (255, 97, 97, 255)
    # from this tuple we need first 3 that are RGB parameters of image
    pixel = d_im.getpixel((x0, y0))[:-1]
    print "Middle pixel coordinates", x0, y0
    print pixel
    # loop through x axis pixels
    count = 0
    max_count = 0
    for x in xrange(sb_im_size[0]):
        for y in xrange(sb_im_size[1]):
            ipixel = sb_im.getpixel((x, y))
            # print "got pixel RGB: {} for pixel:({}, {})".format(ipixel, x, y)
            if ipixel == pixel:
                count += 1
                # print "boooyaa: {}".format(count)
                # if count == icon_squared -5:
                    # print "found square"
            elif count !=0 and max_count<count:
                max_count = count
                max_x = x
                max_y = y
                # draw.rectangle((x - 5, y - 5, x + 5, y + 5), outline='black')
                # print "Current count: {}. Maximum count: {}. Pos = {} {}. Reassigning to 0".format(count, max_count, x, y)
                count = 0
    draw = ImageDraw.Draw(sb_im)
    try:
        draw.rectangle((max_x - x0, max_y - y0, max_x + x0, max_y + y0), outline='yellow')
    except:
        raise EnvironmentError("did not find the button. Failing the test")
    # draw.rectangle((max_x - 16, max_y - 16, max_x + 1, max_y + 1), outline='yellow')
    sb_im.save("found_on_screeshot.png")
    return max_x-x0, max_y-y0

def test_connection_to_vpn():
    resp_before = requests.get("http://curlmyip.net")
    print "Ip before: {}".format(resp_before.text)
    start_hotspot_shield_app()
    time.sleep(5)
    take_screenshot("before_vpn.png")
    button_postion = find_button_position()
    print "Button is located at: ", button_postion
    pyautogui.moveTo(button_postion[0], button_postion[1], duration=2)
    pyautogui.click()
    print "clicked"
    time.sleep(5)
    resp_after = requests.get("http://curlmyip.net")
    print "Ip after: {}".format(resp_after.text)
    assert resp_before!=resp_after.text, "Ip address before connection was equal to Ip address after connection"

if __name__=="__main__":
    # have to launch the script from cmd as Administrator!!!
    test_connection_to_vpn()