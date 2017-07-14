import turtle

fen = turtle.Screen()
fen.setup(width=500, height=500)

def jouer():
    Alex.bouger()
    fen.update()
    fen.ontimer(jouer, 20)

jouer()
fen.listen()
fen.mainloop()
