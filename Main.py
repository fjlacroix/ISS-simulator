import turtle
import Satellite
import math

Rterre = 6371

largeur = 1000
hauteur = largeur

facteur_dechelle = largeur / 15000
dt = 0.1  #secondes réelles écoulées par calcul

fen = turtle.Screen()
fen.setup(width = largeur, height = hauteur)

turtle.speed(0)
turtle.hideturtle()
turtle.penup()
turtle.goto(0, -6371 * facteur_dechelle)
turtle.pendown()
turtle.circle(6371 * facteur_dechelle, steps = 100)


terre2 = turtle.Turtle()
terre2.speed(0)
terre2.hideturtle()
terre2.penup()
terre2.goto((-400 - 6371) * facteur_dechelle * 10, -6371 * facteur_dechelle * 10)
terre2.pendown()
terre2.circle(6371 * facteur_dechelle * 10, steps = 500)


ISSvignette = turtle.Turtle()
ISSvignette.speed(0)
ISSvignette.shape("square")
ISSvignette.color("red")
ISSvignette.shapesize(stretch_len=0.35, stretch_wid=0.5)

Dronevignette = turtle.Turtle()
Dronevignette.speed(0)
Dronevignette.color("blue")
Dronevignette.penup()

Écriture = turtle.Turtle()
Écriture.hideturtle()
Écriture.penup()
Écriture.goto(0,hauteur/3)



ISS = Satellite.Satellite(400, 400, 0, facteur_dechelle, dt)
ISS.color("red")
ISS.shape("square")
ISS.shapesize(stretch_len=0.35, stretch_wid=0.5)

apogéedrone = 410
périgéedrone = 398

adrone = math.sqrt((3.986 * 10 ** 6) * (ISS.P / (2 * math.pi)) ** 2)

if apogéedrone == 0 and périgéedrone != 0:
    apogéedrone = 2 * adrone - (Rterre + périgéedrone) - Rterre
elif périgéedrone == 0 and apogéedrone != 0:
    périgéedrone = 2 * adrone - (Rterre + apogéedrone) - Rterre

Drone = Satellite.Satellite(apogéedrone, périgéedrone, 0.2, facteur_dechelle, dt)
Drone.color("blue")

def animer():
    ISS.avancer()
    ISS.setheading(math.degrees(ISS.nu))
    Drone.avancer()

    deltax = Drone.x - ISS.x
    deltay = Drone.y - ISS.y
    if deltax >=0:
        thetaDronetoISS = 180 + math.degrees(math.atan(deltay / deltax))
        Drone.setheading(thetaDronetoISS)
    else:
        thetaDronetoISS = math.degrees(math.atan((deltay / deltax)))
        Drone.setheading(thetaDronetoISS)

    R = math.sqrt(deltax ** 2 + deltay ** 2)
    thetaISS = ISS.nu + math.pi
    thetatotal = - thetaISS + math.radians(thetaDronetoISS)

    nouveaux = R * math.cos(thetatotal)
    nouveauy = R * math.sin(thetatotal)

    Dronevignette.goto(nouveaux * facteur_dechelle * 10, nouveauy * facteur_dechelle * 10)
    Dronevignette.pendown()
    Dronevignette.setheading(180 + math.degrees(thetatotal))

    Écriture.clear()
    texte = 'Distance ISS-Drone: {} km \n'.format(R)
    Écriture.write(texte)

    fen.update()
    fen.ontimer(animer, 0)

animer()
fen.listen()
fen.mainloop()
