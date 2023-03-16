import random
from vector import Vector

MOVE_RANGE = 50
MOVE_SPEED = 3


class People:
    def __init__(self, engine):
        self.position = Vector(random.randrange(0, engine.size), random.randrange(0, engine.size))
        self.home = self.position.copy()
        self.move_target = self.home.copy()
        self.move_range = MOVE_RANGE
        self.move_speed = MOVE_SPEED
        self.status = "susceptible"

    @property
    def x(self):
        return self.position.x

    @property
    def y(self):
        return self.position.y

    def get_new_target(self):
        self.move_target = self.home + Vector(
            random.uniform(-self.move_range, self.move_range),
            random.uniform(-self.move_range, self.move_range)
        )

        self.step = (self.move_target - self.position).uniform(self.move_speed)

    def move(self):
        if self.position == self.move_target:
            self.get_new_target()

        if (self.move_target - self.position).length < self.move_speed:
            self.position = self.move_target.copy()
        else:
            self.position = self.position + self.step


class Engine:
    def __init__(self, size, population):
        self.size = size
        self.population = population
        self.people = []

    def create(self):
        self.people = []
        for i in range(self.population):
            self.people.append(People(self))

    def next_frame(self):
        for person in self.people:
            person.move()

    def infect(self,number):
        initial_infected
