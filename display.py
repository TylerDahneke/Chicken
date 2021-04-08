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

    return display(root)


class display:

    def __init__(self, master=None):
        self.master = master
        self.canvas = tk.Canvas(master, width=BoardWidth, height=BoardHeight, bg='green')

        self.shapes = shape_wallet.ShapeWallet(self.canvas)

        self.draw_chickens()

        print(f'drew all {self.shapes.get_size()}')
        self.frame_move()

        self.canvas.pack()

    def frame_move(self):
        for shape_node in self.shapes.contents:
            shape_node.move()
        self.canvas.after(500, self.frame_move)

    def draw_chickens(self):
        for y_pos in range(0, BoardHeight, 30):
            for x_pos in range(0, BoardWidth, 30):
                if random.random() > .9:
                    pos1 = x_pos, y_pos
                    pos2 = x_pos + ChickenWidth, y_pos + ChickenHeight
                    self.insert_rectangle(pos1, pos2, fill='white', outline='black')

        self.draw_all_shapes_in_contents()


    def insert_rectangle(self, pos1, pos2, fill=None, outline=None, draw_on_creation=False):
        self.shapes.insert(pos1, pos2, fill=fill, outline=outline, draw_on_creation=draw_on_creation)

    def draw_all_shapes_in_contents(self):
        self.shapes.draw_all()


if __name__ == '__main__':
    main()
