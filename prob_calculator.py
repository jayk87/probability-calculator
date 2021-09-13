import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        self.kwargs = kwargs
        self.contents = []
        for k,v in self.kwargs.items():
            for i in range(v):
                self.contents.append(k)

    def draw(self, amount):
        self.drawn_balls = []
        self.amount = amount
        if self.amount <= len(self.contents):
            for i in range(self.amount):
                rand = random.randrange(len(self.contents))
                self.drawn_balls.append(self.contents[rand])
                self.contents.pop(rand)
            return self.drawn_balls
        else:
            self.drawn_balls = self.contents
            return self.drawn_balls
            
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successful = 0
    probability = None

    for i in range(num_experiments):
        deepcopy = copy.deepcopy(hat)
        deepcopy.draw(num_balls_drawn)
        try:
            for k,v in expected_balls.items():
                for j in range(v):
                    deepcopy.drawn_balls.remove(k)
            successful += 1
        except:
            continue

    probability = (successful / num_experiments)

    return probability
