import p5
from boid import Boid
from config import HEIGHT, WIDTH
flock = []

def setup():
        p5.size(WIDTH, HEIGHT)
        p5.title("flocking")
        i = 0
        while i < 25 :
            flock.append(Boid())
            i += 1


def draw():
        p5.background(51)

        for boid in flock :
            boid.update()
            boid.show()

if __name__ == '__main__':
  p5.run()
  print(flock[0].position)
  print(flock[0].velocity)
  print(flock[0].acceleration)