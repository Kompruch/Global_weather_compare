import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

df = pd.read_csv('/Users/ice/Desktop/Ice data engineer/udacity_project_1/results.csv', delimiter=',')

print(df.head())

# print(df[df.city_temp.isnull()])


df_clean = df.drop(range(0,17)).reset_index(drop=True)


df_clean['5y_moving_avg_city'] = df_clean.city_temp.rolling(5).mean().fillna(0)
df_clean['5y_moving_avg_global'] = df_clean.global_temp.rolling(5).mean().fillna(0)

df_clean['diff_temp'] = df_clean['5y_moving_avg_city'] - df_clean['5y_moving_avg_global']

# print(df_clean['5y_moving_avg_city'].corr(df_clean['5y_moving_avg_global']))
print(df_clean['diff_temp'].mean()) 
print(df_clean['diff_temp'].std()) 
# print(df_clean['city_temp'].mean() / df_clean['global_temp'].mean())
# print(df_clean['city_temp'].mean())
# print(df_clean['global_temp'].mean())
# print(df_clean.head())

year = df_clean.iloc[4:,0]
city_mov = df_clean.iloc[4:,5]
global_mov = df_clean.iloc[4:,6]
diff = df_clean.iloc[4:,7]

# print(year.head(), city_mov.head())


plt.subplot(3, 3, (1,3))
plt.title('5 years mov Bangkok temp')
plt.plot(year, city_mov, label = '5-years moving average city', color='red')
plt.ylabel('Temp in C')
plt.xlabel('year')
plt.legend()

plt.subplot(3, 3, (4,6))
plt.title('5 years mov Global temp')
plt.plot(year, global_mov, label = '5-years moving average global')
plt.ylabel('Temp in C')
plt.xlabel('year')
plt.legend()

plt.subplot(3, 3, (7,9))
plt.title('Difference between 5-years moving average global temperature vs Bangkok temperature')
plt.plot(year, diff, label = 'Difference btween global temperature and Bangkok temperature', color='orange')
plt.ylabel('Temp in C')
plt.xlabel('year')
plt.legend()

plt.tight_layout()
plt.show()
