from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "bold")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.retrieve_highscore()
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset_scoreboard(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.update_highscore(self.score)
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def retrieve_highscore(self):
        with open("data.txt") as read_HS:
            high_score = int(read_HS.read())
        return high_score

    def update_highscore(self, score):
        with open("data.txt", mode="w") as write_HS:
            write_HS.write(str(score))




