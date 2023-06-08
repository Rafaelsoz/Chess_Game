from auxi.const import EDGE


class Position:

    def __init__(self, axis_x, axis_y):
        self.axis_x = axis_x
        self.axis_y = axis_y

    def set_position(self, axis_x, axis_y):
        self.axis_x = axis_x
        self.axis_y = axis_y

    def get_position(self):
        return self.axis_x, self.axis_y


def calc_position(axis):
    return axis[0] // EDGE, axis[1] // EDGE
