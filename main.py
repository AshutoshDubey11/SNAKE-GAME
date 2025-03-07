from tkinter import *
windows = Tk()
windows.title("SNAKE GAME")
windows.minsize(width=620, height=620)
windows.maxsize(width=620, height=620)

front = PhotoImage(file="snake.png")
canvas = Canvas(width=620, height=620)
canvas.create_image(310, 310, image=front)
canvas.create_text(300, 70, text="SNAKE GAME", font=("calibri", 50, "italic"))
canvas.pack()


def play():

    windows.destroy()
    from turtle import Turtle, Screen
    from snake import Snake
    from food import Food
    import time
    from scoreboard import Score
    screen = Screen()
    score = Score()
    tony = Turtle()
    screen.setup(620, 620)
    screen.bgcolor("black")
    screen.title("MY SNAKE GAME")

    screen.tracer(0)
    food = Food()
    snake = Snake()
    tony.penup()
    tony.goto(-300, 300)
    tony.color("blue")
    tony.pendown()
    tony.pensize(10)

    with open("data.txt", "r") as data:
        point = data.read()

    for _ in range(0, 4):
        tony.forward(600)
        tony.right(90)
    tony.hideturtle()

    def game_over():
        snake.color("white")
        if score.k > int(point):
            snake.write("Game Over, New Highscore 🙂", align="center", font=("Arial", 24, "normal"))
        else:
            snake.write("Game Over 😞", align="center", font=("Arial", 24, "normal"))

    def start(game_on=True):
        food.move()

        while game_on:
            screen.update()
            time.sleep(0.1)

            snake.move()
            if snake.head.distance(food) < 15:
                food.move()
                snake.inc()
                score.gain()
            if snake.head.xcor() > 290 or snake.head.ycor() > 290:
                game_on = False
                game_over()
            if snake.head.xcor() < -290 or snake.head.ycor() < -290:
                game_on = False
                game_over()

            for _ in snake.turtles[1:]:
                if snake.head.distance(_) < 10:
                    game_on = False
                    game_over()

    snake.turns()
    screen.listen()
    start()

    screen.exitonclick()


play_button = Button(command=play, text="PLAY", background="lightblue", width=10, font=("calibri", 20, "bold"))
play_button.place(x=260, y=550)

windows.mainloop()
