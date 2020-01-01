import random
import tkinter as tk
import time
import shape_wallet

# GLOBALS

BoardWidth = 600
BoardHeight = BoardWidth

ChickenWidth = 5
ChickenHeight = ChickenWidth


# ENDGLOBALS

def main():
    window = create_display()

    tk.mainloop()


def create_display():
    root = tk.Tk()
    base = display(root)

    root.bind('<KeyPress-b>', lambda _: base.buy_chicken(chicken_amt=5))

    return base


class display:

    def __init__(self, master=None):
        self.master = master
        self.canvas = tk.Canvas(master, width=BoardWidth, height=BoardHeight, bg='green')

        self.shapes = shape_wallet.ShapeWallet(self.canvas)

        self.coins = 0

        self.max_rbg = [254, 254, 254]

        self.buy_chicken(over_ride=True)

        self.frame_move()

        self.canvas.pack()

    def frame_move(self):
        for shape_node in self.shapes.contents:
            self.coins += shape_node.data_type.get_production()
            shape_node.move()
            # print(self.coins)
        self.canvas.after(500, self.frame_move)

    def buy_chicken(self, chicken_amt=1, chicken_cost=1, over_ride=False):
        while chicken_amt:
            if over_ride is True:
                chicken_cost = 0
            else:
                chicken_cost = chicken_cost
            if self.coins < chicken_cost:
                print('CANNOT BUY CHICKEN. INSUFFICIENT FUNDS')
                return False
            else:
                self.coins -= chicken_cost
                self.draw_chicken()
                print(f'BOUGHT CHICKEN {self.max_rbg}. TOTAL IS NOW {self.shapes.get_size()} CHICKENS.')
            chicken_amt -= 1

    def draw_chicken(self):
        x_pos, y_pos = random.randint(0, BoardWidth), random.randint(0, BoardHeight)
        pos1 = x_pos, y_pos
        pos2 = x_pos + ChickenWidth, y_pos + ChickenHeight
        self.insert_rectangle(pos1, pos2, outline='black', draw_on_creation=True)

        self.decrease_max()

    def insert_rectangle(self, pos1, pos2, fill=None, outline=None, draw_on_creation=False):
        if fill is None:
            fill = tuple(self.max_rbg)
        else:
            fill = fill
        self.shapes.insert(pos1, pos2, fill=fill, outline=outline, draw_on_creation=draw_on_creation)

    def draw_all_shapes_in_contents(self):
        self.shapes.draw_all()

    def decrease_max(self):
        roll = random.random()
        counter = 0
        for check_point in self.get_roll_chance():
            if roll <= check_point:
                self.max_rbg[counter] -= 5
                break
            else:
                counter += 1


    def get_roll_chance(self):
        total_rbg_used = 765 - sum(self.max_rbg)
        percent_roll = []
        for index in self.max_rbg:
            index_used = 255 - index
            percent_roll.append(index_used / total_rbg_used)
        print(percent_roll)
        return percent_roll




if __name__ == '__main__':
    main()
