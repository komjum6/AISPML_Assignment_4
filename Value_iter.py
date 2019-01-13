
# coding: utf-8

# In[1]:

import pandas as pd
import numpy as np
import random

from value_iter_helperFuncs import fillWorlds, PreprocessWorlds, PostprocessWorlds, World

if __name__ == "__main__":
	WorldList = fillWorlds()

	PreprocessWorlds(WorldList)

	PostprocessWorlds(WorldList)
