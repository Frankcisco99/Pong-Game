import turtle 

pantalla = turtle.Screen()
pantalla.title("Pong Game")
pantalla.bgcolor("black")
pantalla.setup(600,400)

#paleta izquierda
paleta_izq = turtle.Turtle()
paleta_izq.shape("square")
paleta_izq.color("white")
paleta_izq.shapesize(stretch_len=1,stretch_wid=5)
paleta_izq.penup()
paleta_izq.goto(-250,0)

#paleta derecha
paleta_der = turtle.Turtle()
paleta_der.shape("square")
paleta_der.color("white")
paleta_der.shapesize(stretch_len=1,stretch_wid=5)
paleta_der.penup()
paleta_der.goto(250,0)

def paleta_izq_up():
    y = paleta_izq.ycor()
    y = y + 20
    paleta_izq.sety(y)

def paleta_izq_down():
    y = paleta_izq.ycor()
    y = y - 20
    paleta_izq.sety(y)

def paleta_der_up():
    y = paleta_der.ycor()
    y = y + 20
    paleta_der.sety(y)

def paleta_der_down():
    y = paleta_der.ycor()
    y = y - 20
    paleta_der.sety(y)

pantalla.listen()
pantalla.onkeypress(paleta_izq_up,"w")
pantalla.onkeypress(paleta_izq_down,"s")
pantalla.onkeypress(paleta_der_up,"Up")
pantalla.onkeypress(paleta_der_down,"Down")

while True:
    pantalla.update()

    if paleta_izq.ycor() >= 145:
        paleta_izq.sety(145)
    if paleta_izq.ycor() <= -145:
        paleta_izq.sety(-145)
    if paleta_der.ycor() >= 145:
        paleta_der.sety(145)
    if paleta_der.ycor() <= -145:
        paleta_der.sety(-145)

turtle.done()