
# coding: utf-8

# In[25]:

import pandas as pd
import numpy as np

rowcolList = [5, 10, 20, 50, 100]

for world in rowcolList:
    
    endstate = (world-1, world-1)

    d = pd.DataFrame(np.zeros((world, world)))
    d.iloc[endstate] = 10

    print(d)

