import pgzrun
import random

class Gracz(Actor):
    def __init__(self, x, y):
        super(Gracz, self).__init__("ludzik1", (x, y))
        self.pos = x, y
        self.fps = 0
        self.czy_lustro = False
        self.ruch = False
    def draw(self):
        super(Gracz, self).draw()
    def update(self):
        if self.ruch == False:
            if self.czy_lustro == False:
                self.image = "ludzik1"
            else:
                self.image = "ludzik1l"
    def animacja(self):
        if self.fps == 0:
            if self.czy_lustro == False:
                self.image = "ludzik1"
            else:
                self.image = "ludzik1l"
        if self.fps == 1:
            if self.czy_lustro == False:
                self.image = "ludzik2"
            else:
                self.image = "ludzik2l"
        if self.fps == 2:
            if self.czy_lustro == False:
                self.image = "ludzik3"
            else:
                self.image = "ludzik3l"
        if self.fps == 3:
            if self.czy_lustro == False:
                self.image = "ludzik4"
            else:
                self.image = "ludzik4l"
        if self.fps == 4:
            if self.czy_lustro == False:
                self.image = "ludzik5"
            else:
                self.image = "ludzik5l"
        if self.fps == 5:
            if self.czy_lustro == False:
                self.image = "ludzik6"
            else:
                self.image = "ludzik6l"
        if self.fps == 6:
            if self.czy_lustro == False:
                self.image = "ludzik7"
            else:
                self.image = "ludzik7l"
        if self.fps == 7:
            if self.czy_lustro == False:
                self.image = "ludzik8"
            else:
                self.image = "ludzik8l"
        if self.fps == 8:
            if self.czy_lustro == False:
                self.image = "ludzik9"
            else:
                self.image = "ludzik9l"
        if self.fps == 9:
            if self.czy_lustro == False:
                self.image = "ludzik10"
            else:
                self.image = "ludzik10l"
        if self.fps == 10:
            if self.czy_lustro == False:
                self.image = "ludzik11"
            else:
                self.image = "ludzik11l"
        self.fps += 0.5
        self.fps = self.fps%11
    def lewo(self):
        self.x-=2
        self.czy_lustro = True
        self.animacja()
    def prawo(self):
        self.x+=2
        self.czy_lustro = False
        self.animacja()

class Kowadlo(Actor):
    def __init__(self, x, y):
        super(Kowadlo, self).__init__("kowadlo", (x, y))
        self.x = x
        self.y = y
    def opadanie(self):
        self.y += 2

class Przeszkody():
    def __init__(self):
        self.l=[]
        for i in range(3):
            self.l. append(Kowadlo(random.randint(50, 550), -random.randint(100,500)))
    def update(self):
        for i in self.l:
            i.opadanie()
    def draw(self):
        for i in self.l:
            i.draw()


pulapka = Przeszkody()
howacz = Gracz(100, 507)
def update():
    howacz.update()
    pulapka.update()
    if keyboard.left or keyboard.right:
        if keyboard.left:
            howacz.lewo()
            howacz.ruch = True
        if keyboard.right:
            howacz.prawo()
            howacz.ruch = True
    else:
        howacz.ruch = False
def draw():
    screen.clear()
    screen.fill("#0099ff")
    for i in range(30):
        screen.blit("trawa", (-10+(70*i), 550))
    howacz.draw()
    pulapka.draw()



pgzrun.go()