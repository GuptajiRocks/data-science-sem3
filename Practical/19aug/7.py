import pandas as pd
import numpy as np
# print((pd.Timestamp('11/29/2019') + pd.offsets.MonthEnd()).weekday())

S = pd.Series(np.arange(5), index=['a', 'b', 'c', 'd', 'e'])
print(S['b':'e'])

