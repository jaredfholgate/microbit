from microbit import *

image = Image(
    "0999099999:"
    "0909090000:"
    "0999090000:"
    "0000090000:"
    "0000099999:")

window = Image(5, 5)

def my_scroll(image) :
    for position in range(-4, image.width() + 1):
        for y in range(5):
            for x in range(5):
                window.set_pixel(x, y, image.get_pixel(x + position, y) if 0 <= x + position < image.width() else 0)
        yield window

while True:
    if button_a.was_pressed():
        t = temperature()
        display.scroll(t, wait=True, monospace=False)
        display.show(my_scroll(image), delay=150, wait=True)
