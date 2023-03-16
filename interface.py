import tkinter
from engine import Engine

CANVAS_SIZE = 800
POPULATION = 500


class Interface:
    def __init__(self):
        self.root = tkinter.Tk()
        self.canvas = tkinter.Canvas(self.root, height=CANVAS_SIZE, width=CANVAS_SIZE, bg="white")
        self.canvas.pack()
        self.engine = Engine(CANVAS_SIZE, POPULATION)


    def draw_people(self):
        color = {
            "susceptible": "green",
            "infectious": "red",
            "recovered": "yellow"
        }
        for person in self.engine.people:
            self.canvas.create_rectangle(person.x - 2, person.y - 2, person.x + 2, person.y + 2,
                                         fill=color[person.status],
                                         outline=color[person.status])

    def next_frame(self):
        self.engine.next_frame()
        self.canvas.delete("all")
        self.draw_people()
        self.root.after(30, self.next_frame)

    def start(self):
        self.engine.create()
        self.engine.infect(10)
        self.root.after(30, self.next_frame())
        self.root.mainloop()


if __name__ == '__main__':
    interface = Interface()
    interface.start()
