
from config import height,width
from ball import Ball
import vector

from etc import translate

class Juggle:
    def __init__(self):
        off_set = width/5
        self.hand_left = vector.obj(x=off_set,y=height-100)
        self.hand_right = vector.obj(x=width-off_set,y=height-100)
        self.reset()
        
    def reset(self):
        self.balls = [Ball(self.hand_left.x,self.hand_left.y-100)]

    def step(self,action):
        for b in self.balls:
            b.update()

    def get_inputs(self):
        bx = translate(self.balls[0].pos.x,0,width,-1,1)
        by = translate(self.balls[0].pos.y,0,width,-1,1)
        return [bx,by]