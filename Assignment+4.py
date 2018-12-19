
# coding: utf-8

# In[20]:

import pandas as pd
import numpy as np

d = pd.DataFrame(np.zeros((10, 10)))
d.iloc[9,9] = 10

d2 = pd.DataFrame(np.zeros((5, 5)))
d2.iloc[4,4] = 10

print(d)
print(d2)

