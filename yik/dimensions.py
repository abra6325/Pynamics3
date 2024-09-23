import math


class ClockResizer:

    def __init__(self, value, timescale):
        self.value = value
        self.tick = int(round(value * 60 * timescale, 0))

    def __int__(self):
        return self.tick


class Dimension:

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def format_space_str(target):
        a = list(map(float, target.split(",")))
        return Dimension(a[0], a[1])

    def set(self, x: float, y: float):
        self.x = x
        self.y = y

    def __add__(self, other):
        return self.add(other.x, other.y)

    def __rtruediv__(self, other):
        return Dimension(self.x / other, self.y / other)

    def __truediv__(self, other):
        return self.__rtruediv__(other)

    def add(self, x: float, y: float):
        return Dimension(self.x + x, self.y + y)

    def add_dim(self, dim):
        return Dimension(self.x + dim.x, self.y + dim.y)

    def add_self(self, x: float, y: float):
        self.x += x
        self.y += y

    def distance(self, other):
        return math.sqrt((other.x - self.x) ** 2 + (other.y - self.y) ** 2)

    def add_dim_self(self, dim):
        self.x += dim.x
        self.y += dim.y

    def __repr__(self):
        return f"Dimension({self.x}, {self.y})"

    def __tuple__(self):
        return (self.x, self.y)

    def __getitem__(self, i):
        if i:
            return self.y
        return self.x

    def __eq__(self, other):
        if not isinstance(other, Dimension):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    @property
    def scale_x(self):
        return self.x

    @property
    def offset_x(self):
        return self.y


class Dimension2d:

    def __init__(self, scale_x, offset_x, scale_y, offset_y):
        self.x = Dimension(scale_x, offset_x)
        self.y = Dimension(scale_y, offset_y)

    @property
    def scale_x(self):
        return self.x.scale_x

    @property
    def offset_x(self):
        return self.x.offset_x

    @property
    def scale_y(self):
        return self.y.scale_x

    @property
    def offset_y(self):
        return self.y.offset_x

Dim = Dimension
Dim2d = Dimension2d

class Color(object):

    def __init__(self, r = 255, g = 255, b = 255, a = 0):
        if isinstance(r, str):
            if r.lower() == "white":
                self.r, self.g, self.b = 255, 255, 255
            return

        self.r = r
        self.g = g
        self.b = b
        self.a = a

    def __str__(self):
        return "#%02x%02x%02x" % (int(self.r), int(self.g), int(self.b))

    def __iter__(self):
        return self.r, self.g, self.b

    def __eq__(self, other):
        return self.r == other.r and self.g == other.g and self.b == other.b

    def tuple(self):
        r, g, b, a = self.r + 1, self.g + 1, self.b + 1, self.a + 1
        return (r/256, g/256, b/256, a/256)

    @staticmethod
    def from_float(r, g, b, a):
        return Color(r * 256 - 1, g * 256 - 1, b * 256 - 1, a * 256 - 1)


class Vector:

    """A default rectangular vector data."""

    def __init__(self):
        self.x = 0
        self.y = 0