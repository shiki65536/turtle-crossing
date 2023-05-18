from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def generate(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            car = Turtle()
            car.shape("square")
            car.pu()
            car.shapesize(1, 2)
            car.setheading(180)
            y_axis = random.randint(-250, 250)
            car.setpos(300, y_axis)
            car.color(COLORS[random.randint(0, 5)])
            self.all_cars.append(car)

    def move(self):
        for car in self.all_cars:
            car.fd(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT





