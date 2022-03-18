import vector

class Ball():
    def __init__(self,x,y):
        self.pos = vector.obj(x=x,y=y)
        self.acc = vector.obj(x=1,y=-2.3)
        self.vel = vector.obj(x=0,y=0)
    
    def update(self):
        self.vel = self.vel.add(self.acc)
        self.vel.y+=0.005
        self.pos = self.pos.add(self.vel)
        self.vel.y+=0.005
        self.acc = vector.obj(x=0,y=0)

