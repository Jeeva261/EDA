import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 

# data collecton

file_path=r'C:\Users\ADMIN\OneDrive\Desktop\AIML githup\EDA\dirtydata.csv'
df=pd.read_csv(file_path)
print(df)

# data understanding

file_path=r'C:\Users\ADMIN\OneDrive\Desktop\AIML githup\EDA\dirtydata.csv'
df=pd.read_csv(file_path)
print(df)
print(df.head())
print(df.tail())
print(df.nunique())
print(df.isnull().sum())
print(df.columns)
print(df.describe())
print(df.dtypes)
print(df.info())
print(df.duplicated().sum())


# data cleaning
# fillna

file_path=r'C:\Users\ADMIN\OneDrive\Desktop\AIML githup\EDA\dirtydata.csv'
df=pd.read_csv(file_path)
df=df.fillna(1300)
print(df)

# fillna with mean median mode

file_path=r'C:\Users\ADMIN\OneDrive\Desktop\AIML githup\EDA\dirtydata.csv'
df=pd.read_csv(file_path)
df["Calories"].fillna(df["Calories"].mean(),inplace=True)
print(df)

df=pd.read_csv(file_path)
df["Calories"].fillna(df["Calories"].median(),inplace=True)
print(df)

df=pd.read_csv(file_path)
df["Calories"].fillna(df["Calories"].mode()[0],inplace=True)
print(df)

# dropna

file_path=r'C:\Users\ADMIN\OneDrive\Desktop\AIML githup\EDA\dirtydata.csv'
df=pd.read_csv(file_path)
df.dropna(inplace=True)
print(df)

file_path=r'C:\Users\ADMIN\OneDrive\Desktop\AIML githup\EDA\dirtydata.csv'
df=pd.read_csv(file_path)
df.dropna(subset="Calories",inplace=True)
df.drop("Duration", axis=1, inplace=True)
print(df)


# data format


file_path=r'C:\Users\ADMIN\OneDrive\Desktop\AIML githup\EDA\dirtydata.csv'
df=pd.read_csv(file_path)
df["Date"]=pd.to_datetime(df["Date"])
print(df)


file_path=r'C:\Users\ADMIN\OneDrive\Desktop\AIML githup\EDA\dirtydata.csv'
df=pd.read_csv(file_path)
df["Date"]=pd.to_datetime(df["Date"])
df.dropna(subset="Date",inplace=True)
print(df)


# worng data

file_path=r'C:\Users\ADMIN\OneDrive\Desktop\AIML githup\EDA\dirtydata.csv'
df=pd.read_csv(file_path)
df.loc[7,"Duration"]=10000
print(df)


file_path=r'C:\Users\ADMIN\OneDrive\Desktop\AIML githup\EDA\dirtydata.csv'
df=pd.read_csv(file_path)
for i in df.index:
    if df.loc[i,"Duration"]>120:
        df.loc[i]=1000
print(df)


file_path=r'C:\Users\ADMIN\OneDrive\Desktop\AIML githup\EDA\dirtydata.csv'
df=pd.read_csv(file_path)
for i in df.index:
    if df.loc[i,"Duration"]>120:
        df.drop(i,inplace=True)
print(df)


# remove duplicates

file_path=r'C:\Users\ADMIN\OneDrive\Desktop\AIML githup\EDA\dirtydata.csv'
df=pd.read_csv(file_path)
df.drop_duplicates(inplace=True)
print(df)

# replace

file_path=r'C:\Users\ADMIN\OneDrive\Desktop\AIML githup\EDA\dirtydata.csv'
df=pd.read_csv(file_path)
df["Duration"]=df["Duration"].replace(60,1200)
print(df)

# corr

file_path=r'C:\Users\ADMIN\OneDrive\Desktop\AIML githup\EDA\file1.csv'
df=pd.read_csv(file_path)
print(df.corr())

# save files

file_path=r'C:\Users\ADMIN\OneDrive\Desktop\AIML githup\EDA\file1.csv'
df=pd.read_csv(file_path)
df.to_csv("demo.csv")


# Data transfer

file_path=r'C:\Users\ADMIN\OneDrive\Desktop\AIML githup\EDA\dirtydata.csv'
df=pd.read_csv(file_path)
df["Duration"]=df['Duration'].astype("f")
print(df)

file_path=r'C:\Users\ADMIN\OneDrive\Desktop\AIML githup\EDA\dirtydata.csv'
df=pd.read_csv(file_path)
df["new_date"]=df["Maxpulse"]*df["Pulse"]
print(df)

# groupby
# single grouping

file_path=r'C:\Users\ADMIN\OneDrive\Desktop\AIML githup\EDA\file.csv'
df=pd.read_csv(file_path)
groupby = df.groupby(["Name"]).sum()
print(groupby)

# mulit grouping

file_path=r'C:\Users\ADMIN\OneDrive\Desktop\AIML githup\EDA\file.csv'
df=pd.read_csv(file_path)
groupby=df.groupby(["Name","Gender"])["Age"].count()
print(groupby)

agg=df.groupby(["Name","Gender"]).agg({
    "Age":["size","sum","mean","median","count"]

})
print(agg)



# data visualization

file_path=r'C:\Users\ADMIN\OneDrive\Desktop\AIML githup\EDA\file.csv'
df=pd.read_csv(file_path)
print(df)

# line plot

sns.lineplot(x="Age",y="number",data=df,marker="o",linestyle=":",hue="Gender")
plt.show()

# barplot
sns.barplot(x="Name",y="Age",data=df,color="red",hue="Gender")
plt.show()

# histogram
sns.histplot(df["Age"],kde=True,bins=10,color="blue")
plt.show()

# scatterplot
sns.scatterplot(x="Age",y="number",data=df,hue="Gender")
plt.show()