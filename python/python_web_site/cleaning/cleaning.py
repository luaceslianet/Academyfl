import pandas as pd

df = pd.read_csv('D:\portfolio\Academyfl\python\python_web_site\cleaning\data1.csv')

new_df = df.dropna()

print(new_df.to_string())


x = df["Calories"].mean()


df.drop_duplicates(inplace = True)