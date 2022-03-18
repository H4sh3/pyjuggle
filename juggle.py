
from config import height,width
from ball import Ball
from etc import translate
import numpy

class Juggle:
    def __init__(self):
        off_set = width/5
        self.hand_left = numpy.array([off_set,height-100])
        self.hand_right = numpy.array([width-off_set,height-100])
        self.reset()
        
    def reset(self):
        self.done = False
        self.data = []
        self.balls = [Ball(self.hand_left[0],self.hand_left[1]-100)]

    def step(self):

        ball = self.balls[0]
        dist_left = numpy.linalg.norm(ball.pos-self.hand_left)
        dist_right = numpy.linalg.norm(ball.pos-self.hand_right)

        if(dist_right < 50):
            # hit target
            self.done = True
            

        if(dist_left < 50):
            inputs = self.get_inputs()
            outputs = self.nn.forward(inputs)
            ball.acc[0] = outputs[0]
            ball.acc[1] = outputs[1]
            self.data.append(
                {
                    "inputs":inputs,
                    "outputs":outputs
                }
            )


        for b in self.balls:
            b.update()

    def get_inputs(self):
        bx = translate(self.balls[0].pos[0],0,width,-1,1)
        by = translate(self.balls[0].pos[1],0,height,-1,1)
        return [bx,by]