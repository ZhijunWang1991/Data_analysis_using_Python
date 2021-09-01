# Reference https://www.zhihu.com/question/33783546

import pandas as pd

df = pd.read_csv('XY_code.csv')

df.head()

BBox = ((df.longitude.min(),   df.longitude.max(),
         df.latitude.min(), df.latitude.max())

