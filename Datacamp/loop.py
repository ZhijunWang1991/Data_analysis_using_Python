# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 11:26:46 2021

@author: wang298
"""

##Loop

# Import numpy as np
import numpy as np

# For loop over np_height
for x in np_height:
    print(str(x)+ " inches")

# For loop over np_baseball
for x in np.nditer(np_baseball):
    print(x)