
# coding: utf-8

# In[1]:

import pandas as pd
import numpy as np
import random

from value_iter_helperFuncs import fillWorlds, PreprocessWorlds, PostprocessWorlds, World

WorldList = fillWorlds()

PreprocessWorlds(WorldList)

PostprocessWorlds(WorldList)
    
# WORLDS
# obstacles
# x * y
# number of endstates
# negative endstates

# DISCOUNTS
# discount values

# REWARDS
# reward values

# PROBABILITIES
# transition probabilities

