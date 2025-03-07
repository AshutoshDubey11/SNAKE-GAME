from turtle import Turtle

with open("data.txt", "r") as data:
    point = data.read()


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.k = 0
        self.color("light green")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.write(f"Score : {self.k}    High Score : {point}", align="center", font=("Arial", 15, "normal"))
        self.hideturtle()

    def gain(self):
        self.k = self.k + 1
        self.clear()
        if self.k > int(point):
            with open("data.txt", "w") as file:
                file.write(f"{self.k}")
            with open("data.txt", "r") as file:
                new_point = file.read()
            self.write(f"Score : {self.k}    High Score : {new_point}", align="center", font=("Arial", 15, "normal"))

        else:
            self.write(f"Score : {self.k}    High Score : {point}", align="center", font=("Arial", 15, "normal"))
