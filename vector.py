class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def copy(self):
        return Vector(self.x, self.y)

    def __add__(self, other):
        # v3  = v1 + v2
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    @property
    def length(self):
        return (self.x * self.x + self.y * self.y) ** 0.5

    def uniform(self, length):
        return Vector(self.x / self.length * length, self.y / self.length * length)
