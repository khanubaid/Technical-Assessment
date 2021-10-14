import pandas as pd
import seaborn as sns
sns.set(color_codes=True)
data = pd.read_csv('table.csv')
data.head()
sns.pairplot(data[['Cust_I', 'Open_Dt', 'DOB']])