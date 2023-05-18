import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.generate()
    car.move()

    for c in car.all_cars:
        if player.distance(c.pos()) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.at_finish():
        player.back_zero()
        car.level_up()
        scoreboard.update_score()



screen.exitonclick()