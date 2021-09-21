import pandas as pd

data = {'area': ['new-hills', 'cape-town', 'mumbai'],
        'rainfall': [100, 70, 200],
        'temperature': [20, 25, 39]}

df = pd.DataFrame.from_dict(data, orient='index')
df
print(df)