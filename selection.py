import pandas as pd
'''df = pd.read_csv("Pokemon.csv")
#selecting a specific column
print(df["Name"].to_string())
print(df["Type 1"].to_string())
print(df["Type 2"].to_string())
print(df["Name", "Type 1", "Type 2"].to_string())
print(df.loc[0:10].to_string())
print(df.iloc[0:10:2,0:4].to_string())
'''
#Searching for a specific value
df=pd.read_csv("Pokemon.csv",index_col="Name")
pokemon_name=input("Enter the Pokemon name: ")
try:
    print(df.loc[pokemon_name].to_string())
except KeyError:
    print("Pokemon not found in the dataset.")


