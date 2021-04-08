import random


def _from_rgb(rgb):
    """translates an rgb tuple of int to a tkinter friendly color code
    """
    return "#%02x%02x%02x" % rgb


class Chicken:

    def __init__(self, rgb=None, speed=3):
        if rgb is None:
            self.rgb = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        else:
            self.rgb = rgb

        self.speed = speed

    def get_tk_color(self):
        return _from_rgb(self.rgb)

    def get_move_delta(self):
        return random.randint(-1, 1) * self.speed, random.randint(-1, 1) * self.speed
