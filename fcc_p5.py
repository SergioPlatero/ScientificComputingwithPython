### PROBABILITY PROJECT ###
from copy import deepcopy, copy
import random
random.seed(101)

# The following class should take a variable number of arguments, that
# specify the number of balls of each color that are in the hat.

class Hat: 
    """
    Takes a variable number of arguments that specify the number of
    balls of each color that are in the hat.
    """
    def __init__(self, **args):
        self.balls = args
        self.contents= []
        for key in self.balls:
            while self.balls[key] > 0:
                self.contents.append(key)
                self.balls[key] -= 1

    def draw(self, num):
        """
        Argument indicates how many balls you wish to 'draw from the hat'.
        Removes balls at random from contents, and returns those
        balls as a list of strings.
        Note: Should this number exceed the available quantity of balls,
        all balls will be returned. If not, they will be removed from contents
        similar to an urn experiment without replacement.
        """
        drawList = []
        num = num
        temp = ""
        
        if num >= len(self.contents):
            drawList = list(self.contents)
            return drawList
        
        else:
            while num > 0:
                temp = random.choice(self.contents)
                drawList.append(temp)
                self.contents.remove(temp)
                num -= 1
                
            return drawList

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    """
    This function takes the following arguments:
    1) hat: a hat object containing balls should be copied here
    2) expected_balls: a dict object indicating the exact group of balls to attempt
    to draw from the hat for the experiment. For example, if you wanted to draw 1 blue
    ball and 1 green ball, expected_balls would equal {'blue':2, 'red':1}
    3) num_balls_drawn: This is the number of balls you wish to draw from the hat in
    each experiment
    4) num_experiments: This is how many times you would like to run the experiment.
    The more you run, the more accurate the approximate probability will be.
    """
    resetHat = deepcopy(hat)
    hat = copy(hat)
    tempList = []
    expectedList = []
    drawNum = num_balls_drawn
    count = num_experiments
    N = num_experiments
    M = 0



    for key in expected_balls:
        while expected_balls[key] > 0:
            expectedList.append(key)
            expected_balls[key] -= 1

    while count > 0:
        tempList = hat.draw(drawNum)
        for item in expectedList:
            if expectedList.count(item) <= tempList.count(item):
                continue
            else:
                break
        else:
            M += 1
        count -= 1
        hat = deepcopy(resetHat)

    return M/N
        

    
      
# The following code is a test
hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat, 
                  expected_balls={"red":2,"green":1},
                  num_balls_drawn=5,
                  num_experiments=10)
