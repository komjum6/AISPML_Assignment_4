import pandas as pd
import numpy as np
import random

class World:
    def __init__(self, Xdimension, Ydimension, obstacles, Nendstates, endstates, negativeEndstates, discount, reward, transitionProbs, Grid):
        self.Xdimension = Xdimension
        self.Ydimension = Ydimension
        self.obstacles = obstacles
        self.Nendstates = Nendstates
        self.endstates = endstates
        self.negativeEndstates = negativeEndstates
        self.discount = discount
        self.reward = reward
        self.transitionProbs = transitionProbs
        self.Grid = Grid
        
    def SetGrid(self, Grid):
        self.Grid = Grid
    
        
def fillWorlds():
    WorldList = []
    #colList = random.sample(range(1, 101), 10) #Generates a list of 10 elements with a number of columns according to the set threshold
    #rowList = random.sample(range(1, 101), 10) #Generates a list of 10 elements with a number of rows according to the set threshold

    colList = random.sample(range(1, 21), 10) #Generates a list of 10 elements with a number of columns according to the set threshold
    rowList = random.sample(range(1, 21), 10) #Generates a list of 10 elements with a number of rows according to the set threshold

    obstacles = [bool(random.getrandbits(1)) for x in range(0, 10)]
    #Nendstates = [bool(random.getrandbits(1)) for x in range(0, 10)]


    for col, row in zip(colList, rowList):
        WorldList.append(World(col, row, obstacles, Nendstates=None, endstates=None, negativeEndstates=None, discount=None, reward=None, transitionProbs=None, Grid=None))
    
    return WorldList

def PreprocessWorlds(WorldList):
    for World in WorldList:
    
        endstate = (World.Xdimension-1, World.Ydimension-1)

        #d = pd.DataFrame(np.zeros((World.Xdimension, World.Ydimension)))
        grid = pd.DataFrame(np.random.randint(3,10,size=(World.Xdimension, World.Ydimension)))

        grid.iloc[endstate] = 10
        
        World.SetGrid(grid)

        print("\n", grid)

def PostprocessWorlds(WorldList):
    print("eey")