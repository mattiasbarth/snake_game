from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


def read_highscore():
    with open("data.txt") as file:
        data = int(file.read())
    return data


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = read_highscore()
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.update_scoreboard()
        self.hideturtle()


    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align=ALIGNMENT, font=FONT)


    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            self.save_highscore()
            self.clear()
        self.score = 0
        self.update_scoreboard()


    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def save_highscore(self):
        with open("data.txt", "w") as file:
            file.write(str(self.highscore))
