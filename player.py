from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.pu()
        self.back_zero()

    def go_up(self):
        self.fd(MOVE_DISTANCE)

    def at_finish(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

    def back_zero(self):
        self.setpos(STARTING_POSITION)
