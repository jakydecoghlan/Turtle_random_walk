import turtle as t
import random

miguel_angel = t.Turtle()
t.colormode(255)

########### Challenge 4 - Random Walk ########
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
angles = [0, 90, 180, 270]
miguel_angel.speed(9)
miguel_angel.pensize(10)

def random_walk():
    miguel_angel.pencolor(random.randint (0,255), random.randint (0,255), random.randint (0,255) )
    miguel_angel.forward(random.randint(1,30))
    miguel_angel.left(random.choice(angles))


caminata = True
while caminata:
    random_walk()

screen = t.Screen()
screen.exitonclick()