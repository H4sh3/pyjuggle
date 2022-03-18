import numpy

class Ball():
    def __init__(self,x,y):
        self.pos = numpy.array([x,y])
        self.acc = numpy.array([.0,.0])
        self.vel = numpy.array([.0,.0])
    
    def update(self):
        self.vel += self.acc
        self.vel[1]+=0.002
        self.pos += self.vel
        self.vel[1]+=0.002
        self.acc = numpy.array([.0,.0])

