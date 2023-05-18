from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pu()
        self.level = 0
        self.setpos(-280, 260)
        self.update_score()

    def update_score(self):
        self.level += 1
        self.clear()
        self.write(f"Level {self.level}", font=FONT)

    def game_over(self):
        self.setpos(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
