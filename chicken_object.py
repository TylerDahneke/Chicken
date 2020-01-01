import random
import math


def _from_rgb(rgb):
    """translates an rgb tuple of int to a tkinter friendly color code
    """
    return "#%02x%02x%02x" % rgb


def calc_del(old_pos, new_pos):
    old_x, old_y = old_pos
    new_x, new_y = new_pos

    return math.pow(math.pow(new_x - old_x, 2) + math.pow(new_y - old_y, 2), .5)

def partition(arr, center, low, high):
    i = (low - 1)  # index of smaller element
    pivot = arr[high]  # pivot

    for j in range(low, high):

        # If current element is smaller than or
        # equal to pivot
        if calc_del(center, arr[j].pos1) <= calc_del(center, pivot.pos1):

            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)


# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index

# Function to do Quick sort


def quickSort(arr, center, low=None, high=None):
    if low is None:
        low = 0
    else:
        low = low
    if high is None:
        high = len(arr) - 1
    else:
        high = high
    if len(arr) == 1:
        return arr
    if low < high:
        # pi is partitioning index, arr[p] is now
        # at right place
        if center != 0:
            pi = partition(arr, center, low, high)


            # Separately sort elements before
            # partition and after partition
            quickSort(arr, low, pi - 1)
            quickSort(arr, pi + 1, high)




class Chicken:

    def __init__(self, pos1, rgb=None, speed=3):

        self.x, self.y = self.pos = pos1

        if rgb is None:
            self.r, self.g, self.b = self.rgb = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        else:
            self.r, self.g, self.b = self.rgb = rgb

        self.production = self.get_production()

        self.speed = speed


    def __repr__(self):
        return f'{self.production}'

    def get_tk_color(self):
        return _from_rgb(self.rgb)

    def get_move_delta(self):
        return random.randint(-1, 1) * self.speed, random.randint(-1, 1) * self.speed

    def update_pos(self, pos):
        self.x, self.y = self.pos = pos

    def get_production(self):
        base_vari = math.pow(math.pow((255 - self.r) / 255, 2) + math.pow((255 - self.g) / 255, 2) + \
                             math.pow((255 - self.b) / 255, 2), .5)
        production_scalar = 50
        return base_vari * production_scalar

