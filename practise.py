# Perform EDA on a dataset and summarize the findings

import pandas as pd

df=pd.read_csv("dirtydata.csv")
print(df.head())
print(df.tail())
print(df.info())
print(df.describe())
print(df.isnull())
print(df.isnull().sum())
print(df.columns)
print(df.duplicated())
print(df.duplicated().sum())
print(df.nunique())

df=pd.read_csv("dirtydata.csv")
df.fillna(100000,inplace=True)
print(df)

df=pd.read_csv("dirtydata.csv")
df.dropna(inplace=True)
print(df)

df=pd.read_csv("dirtydata.csv")
df.dropna(subset=["Calories"],inplace=True)
print(df)

df=pd.read_csv("dirtydata.csv")
res=df["Calories"].mode()[0]
df["Calories"].fillna(res,inplace=True)
print(df)

df=pd.read_csv("dirtydata.csv")
df.loc[7,"Duration"]=1300
print(df)

df=pd.read_csv("dirtydata.csv")
for i in df.index:
    if df.loc[i,"Duration"]>120:
        df.drop(i,inplace=True)
print(df)

df=pd.read_csv("dirtydata.csv")
df["Date"]=pd.to_datetime(df["Date"])
df.dropna(subset="Date",inplace=True)
print(df)

df=pd.read_csv("dirtydata.csv")
df.fillna(df["Calories"].mean(),inplace=True)
df["Calories"]=df["Calories"].astype("i")
print(df)

df=pd.read_json("opendata.json")
print(df.corr())


df=pd.read_csv("dirtydata.csv")
data=df.groupby("Maxpulse").count()
print(data)


df=pd.read_csv("dirtydata.csv")
data=df.groupby(["Maxpulse","Duration"])["EName"].count()
print(data)

df=pd.read_csv("file.csv")
filter=df[df["Duration"]>60]
print(filter)

df=pd.read_csv("file.csv")
sorted=df.sort_values("EName")
print(sorted)

df=pd.read_csv("file.csv")
data=df.groupby("Duration")["EName"].mean()
print(data)

df=pd.read_csv("file.csv")
data=df.groupby("Duration").agg({
    "EName":["mean","median","sum","max","min"]
})
print(data)


import seaborn as sns
import matplotlib.pyplot as plt
# Visualize the distribution of a numerical column using histograms

file_path=r'C:\Users\ADMIN\OneDrive\Desktop\AIML githup\EDA\dirtydata.csv'
df=pd.read_csv(file_path)

sns.histplot(df["Duration"],kde=True,bins=20)
plt.show()