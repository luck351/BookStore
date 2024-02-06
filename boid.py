from config import DOTSIZE, HEIGHT, WIDTH
import p5
import random
class Boid() :

    def __init__(self) :
        self.position = p5.vector.Vector(WIDTH/2,HEIGHT/2)
        #self.velocity = p5.vector.Vector(random.uniform(-1,1),random.uniform(-1,1))
        self.velocity = p5.vector.Vector.random_2D()
        #self.velocity.magnitude = random.uniform(0.5,1.5)
        self.acceleration = p5.vector.Vector(0,0)
        
    
    def update(self) :
        #print(self.position[:])
        self.position += self.velocity
        #print(self.position[:])
        self.velocity += self.acceleration

    def show(self) :
        p5.stroke_weight(DOTSIZE)
        p5.stroke(255)
        p5.point(self.position.x,self.position.y)
       