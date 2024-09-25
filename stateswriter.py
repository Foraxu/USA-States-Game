from turtle import Turtle

FONT='Arial'
FONT_SIZE=8

class Stateswriter(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pu()

    def draw_state_name(self, state_name: str, coords: tuple):
        self.goto(coords)
        self.write(state_name, align='center', move=False, font=(f'{FONT}', FONT_SIZE, 'normal'))