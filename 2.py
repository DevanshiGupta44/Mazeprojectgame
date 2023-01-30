import turtle
import math
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Maze Game")
wn.setup(700,700)

class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("yellow")
        self.penup()
        self.speed(0)
#speed doesnt mean object speed, it means animation ki speed

class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("circle")
        self.color("pink")
        self.penup()
        self.speed(0)
    
    def go_up(self):
        move_to_x = player.xcor()
        move_to_y = player.ycor() + 24
        if (move_to_x,move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)

    def go_down(self):
        move_to_x = player.xcor()
        move_to_y = player.ycor() - 24
        if (move_to_x,move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)
    
    def go_left(self):
        move_to_x = player.xcor() - 24
        move_to_y = player.ycor() 
        if (move_to_x,move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)

    def go_right(self):
        move_to_x = player.xcor() + 24
        move_to_y = player.ycor() 
        if (move_to_x,move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)


    def go_up(self):
        self.goto(self.xcor(), self.ycor() +24)
    def go_down(self):
        self.goto(self.xcor(), self.ycor() -24)
    def go_left(self):
        self.goto(self.xcor() - 24, self.ycor())
    def go_right(self):
        self.goto(self.xcor() +24, self.ycor())

    def is_collision(self, other):
        a = self.xcor()-other.xcor()
        b = self.ycor()-other.xcor()
        distance = math.sqrt((a**2) + (b**2))

        if distance < 5:
            return True
        else:
            return False

class Treasure(turtle.Turtle):
    def __init__(self,x,y):
        turtle.Turtle.__init__(self)
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed(0)
        self.gold = 100
        self.goto(x,y)
    def destroy(self):
        self.goto(2000,2000)
        self.hideturtle()


levels = [""]
#P is for player= matlab player waha start karega in maze layout(pink)
#T to represent treasure (white)
level_1 = [
"XXXXXXXXXXXXXXXXXXXX",
"X P  XXXXXXXXXXXXXXX",
"XX   XXXXXX    XX  X",
"XX       XX        X",
"XXXXXX   XXXX   X  X",
"XX  XX   XXXX   XXXX",
"XX              XXXX",
"XXXXXXXXX    XXXX  X",
"XXX   XXX    XXXX  X",
"XXX   XXX    XXXX  X",
"XXX          XXXX  X",
"XXXXXXXXX          X",
"XXXX           XXXXX",
"XXXX    XXXXXXXXXXXX",
"XXXX    XXXX   XX TX",
"XX             XX  X",
"XXXXXXXXXXXX       X",
"XXXXXX           XXX",
"XX       XX    XXXXX",
"XXXXXXXXXXXXXXXXXXXX"
]

treasures = []
levels.append(level_1)

def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            character = level[y][x]
            screen_x = -288 + (x * 24)
            screen_y = 288 - (y * 24)

            if character =="X":
                pen.goto(screen_x,screen_y)
                pen.stamp()
                walls.append((screen_x,screen_y))
            
            if character == "P":
                player.goto(screen_x,screen_y)
            
            if character == "T":
                treasures.append(Treasure(screen_x,screen_y))

pen = Pen()
player = Player()
walls = []
#setting up level
setup_maze(levels[1])
print(walls)

#keyboard binding
turtle.listen()
turtle.onkey(player.go_left,"Left")
turtle.onkey(player.go_right,"Right")
turtle.onkey(player.go_up,"Up")
turtle.onkey(player.go_down,"Down")

wn.tracer(0)

#main game loop
while True:
    for treasure in treasures:
        if player.is_collision(treasure):
            player.gold +=treasure.gold
            print("Player Gold: {}".format(player.gold))
            treasure.destroy()
            treasures.remove(treasure)
    wn.update()

