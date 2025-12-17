#data cleaning = process of detecting and correcting (or removing) corrupt or inaccurate records from a dataset.
import pandas as pd
df = pd.read_csv("Pokemon.csv")
#drop irrelevant column
'''df=df.drop(columns=["Legendary","#"])
print(df)
#handle missing values
df=df.dropna(subset=["Type 2"]) #drop rows with missing Type 2
print(df)
df=df.fillna({"Type 2":"NULLL"}) #fill missing Type 2 with NULLL
print(df)

#fixing inconsistent data
df["Type 1"]=df["Type 1"].replace({"Fire":"FIRE","Water":"WATER "})
print(df.to_string())
df["Type 1"]=df["Type 1"].str.strip() #remove leading/trailing spaces
print(df.to_string())

#Standardizing data
df["Name"]=df["Name"].str.lower() #convert to lowercase
print(df.to_string())'''

#Fix data types
df["Legendary"]=df["Legendary"].astype(int) #convert to boolean
print(df.to_string())

#Drop duplicates
df=df.drop_duplicates() #drop duplicate rows
print(df.to_string())