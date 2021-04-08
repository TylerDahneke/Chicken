import chicken_object as c_o


class ShapeNode:

    def __init__(self, canvas, pos1, pos2, data_type=None,
                 fill=None, outline=None, draw_on_creation=False):
        self.canvas = canvas

        if fill is None:
            self.fill = ''
        else:
            self.fill = fill
        if outline is None:
            self.outline = ''
        else:
            self.outline = outline

        self.x, self.y = self.pos1 = pos1
        self.x_2, self.y_2 = self.pos2 = pos2

        self.data_type = c_o.Chicken(self.pos1, fill)

        if draw_on_creation:
            self.canvas_shape_id = None
            self.draw()
        else:
            self.canvas_shape_id = None

    def __eq__(self, other):
        return self.canvas_shape_id == other.canvas_shape_id

    def __repr__(self):
        return f'[{self.pos1}, {self.data_type.production}]'

    def draw(self):
        self.canvas_shape_id = self.canvas.create_rectangle(self.x, self.y, self.x_2, self.y_2,
                                                            fill=self.data_type.get_tk_color(), outline=self.outline)

    def move(self):
        if self.canvas_shape_id is None:
            return False
        del_x, del_y = self.data_type.get_move_delta()
        self.canvas.move(self.canvas_shape_id, del_x, del_y)
        self.x += del_x
        self.x_2 += del_x
        self.y += del_y
        self.y_2 += del_y
        self.pos1 = self.x, self.y
        self.pos2 = self.x_2, self.y_2
        self.data_type.update_pos(self.pos1)

    def assign_fill(self, fill_str):
        self.fill = fill_str

    def assign_outline(self, outline_str):
        self.outline = outline_str


class ShapeWallet:

    def __init__(self, canvas):
        self.canvas = canvas
        self.contents = []
        self.num_items = 0

    def draw_all(self):
        for node in self.contents:
            node.draw()

    def insert(self, pos1, pos2, fill=None, outline=None, draw_on_creation=False):
        new_shape_node = ShapeNode(self.canvas, pos1, pos2, fill=fill, outline=outline,
                                   draw_on_creation=draw_on_creation)
        self.contents.append(new_shape_node)
        self.num_items += 1

    def pop(self, index=-1):
        ph, self.contents = self.contents[index], self.contents[:index]
        self.num_items -= 1
        return ph

    def get_index(self, canvas_id):
        counter = 0
        for node in self.contents:
            if node.canvas_shape_id == canvas_id:
                return counter
            counter += 1
        return -1

    def get_size(self):
        return self.num_items

    def is_empty(self):
        return not self.num_items