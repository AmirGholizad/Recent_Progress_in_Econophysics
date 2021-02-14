import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import datetime
import pytz

T = 7
RETURNS = np.zeros(1)
df = pd.read_csv(r'C:\Users\TheAMG\Projects\econophysics\S_Mobarakeh.Steel.csv')
print((df['<CLOSE>'][1]-df['<CLOSE>'][1+T])/df['<CLOSE>'][1+T])
for i in range(0,len(df)-T):
    RETURNS = np.append(RETURNS, (df['<CLOSE>'][i]-df['<CLOSE>'][i+T])/df['<CLOSE>'][i+T])
RETURNS = RETURNS[1:]
print(RETURNS[0:20])

sns.distplot(RETURNS, norm_hist = True, bins=1000)
plt.show()