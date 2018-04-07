import matplotlib.pyplot as plt
from random import choice
class RandomWalk():
    def __init__(self):
        self.x=[0]
        self.y=[0]
        self.num_points=5000

    def fill_walk(self):
        while len(self.x)<self.num_points:
            x_direction = choice([1,-1]) #random.choice需要的是序列，list
            x_distance = choice([1,2,3,4])
            x_step = x_direction*x_distance
            y_direction = choice([1,-1])
            y_distance = choice([1,2,3,4])
            y_step = y_direction*y_distance
            if x_step == 0 and y_step == 0:
                continue

            next_x = self.x[-1]+x_step
            next_y = self.y[-1] + y_step
            self.x.append(next_x)
            self.y.append(next_y)

p = RandomWalk()
p.fill_walk()
plt.scatter(p.x,p.y,s=15)