import turtle
import math

#On fait l'hypothèse que les orbites sont coplanaires.
# Puisque l'orbite de l'ISS est circulaire, pas besoin de calculer les arguments de périgée et les ascention droite du noeud ascendant.

class Satellite(turtle.Turtle):
    def __init__(self, apogée, périgée, nu, facteur, dt):
        super().__init__()
        rterre = 6371
        muterre = 3.986 * (10 ** 6)
        self.apogée = apogée + rterre
        self.périgée = périgée + rterre
        self.nu = math.radians(nu)
        self.facteur = facteur
        self.dt = dt
        self.a = (self.apogée + self.périgée) / 2
        self.c = self.apogée - self.périgée
        if self.apogée == self.périgée:
            self.e = 1
            self.R = self.apogée
        else:
            self.e = (2 * self.c) / (2 * self.a)
            self.R = (self.a * (1 - (self.e) ** 2)) / (1 + self.e * math.cos(self.nu))
        self.x = self.R * math.cos(self.nu)
        self.y = self.R * math.sin(self.nu)
        self.P = 2 * math.pi * math.sqrt((self.a ** 2) / muterre)
        self.n = 2 * math.pi / self.P
        self.speed(0)
        self.penup()
        self.goto(self.x * self.facteur, self.y * self.facteur)
        self.pendown()
        self.M = self.nu
        self.E = self.M


    def ligne_directe(self,sat2):
        self.x2 = sat2.R * math.cos(sat2.nu)
        self.y2 = sat2.R * math.sin(sat2.nu)
        distance = math.sqrt((self.x - self.x2) ** 2 + (self.y - self.y2) ** 2)
        return(distance)

    def avancer(self):
        if self.e == 1:
            self.nu += self.dt * self.n
            self.x = self.R * math.cos(self.nu)
            self.y = self.R * math.sin(self.nu)
            self.goto(self.x * self.facteur, self.y * self.facteur)

        else:
            if self.M > 2 * math.pi:
                self.M -= 2 * math.pi
            if self.E > 2 * math.pi:
                self.E -= 2* math.pi
            self.M += self.n * self.dt
            for i in range(20):
                self.E = self.M + self.e * math.sin(self.E)

            if self.M > math.pi and self.M < 2 * math.pi:
                self.nu = (2 * math.pi) - math.acos((math.cos(self.E) - self.e) / (1 - (self.e * math.cos(self.E))))

            else:
                self.nu = math.acos((math.cos(self.E) - self.e) / (1 - (self.e * math.cos(self.E))))

            self.R = (self.a * (1 - (self.e) ** 2)) / (1 + self.e * math.cos(self.nu))
            self.x = self.R * math.cos(self.nu)
            self.y = self.R * math.sin(self.nu)


            self.goto(self.x * self.facteur, self.y * self.facteur)


