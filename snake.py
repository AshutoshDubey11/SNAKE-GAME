from turtle import Turtle, Screen
X = [0, -20, -40]
screen = Screen()


class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.turtles = []
        self.k = 2
        self.create_snake()
        self.head = self.turtles[0]
        self.hideturtle()

    def create_snake(self):
        for _ in range(0, 3):
            tony = Turtle()
            tony.shape("square")
            tony.color("white")
            tony.penup()
            tony.goto(X[_], 0)
            self.turtles.append(tony)

    def inc(self):
        tony = Turtle()
        tony.shape("square")
        tony.color("black")
        tony.penup()
        self.turtles.append(tony)
        self.k += 1

    def move(self):
        for turtle in range(len(self.turtles) - 1, 0, -1):
            self.turtles[self.k].color("white")
            new_x = self.turtles[turtle - 1].xcor()
            new_y = self.turtles[turtle - 1].ycor()
            self.turtles[turtle].goto(new_x, new_y)
        for turtle in range(0, len(self.turtles)):
            if turtle % 2 == 0:
                self.turtles[turtle].color("red")
        self.head.forward(20)

    def turns(self):
        def turn_left():
            self.turtles[0].setheading(180)

        def turn_up():
            self.turtles[0].setheading(90)

        def turn_down():
            self.turtles[0].setheading(270)

        def turn_right():
            self.turtles[0].setheading(0)

        screen.listen()
        screen.onkey(key="Up", fun=turn_up)
        screen.onkey(key="Left", fun=turn_left)
        screen.onkey(key="Down", fun=turn_down)
        screen.onkey(key="Right", fun=turn_right)
