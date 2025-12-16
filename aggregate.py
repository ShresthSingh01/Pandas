#Aggregate = function that combines multiple inputs into a single output.
import pandas as pd
df = pd.read_csv("Pokemon.csv")
#Aggregate functions = count, mean, median, min, max, sum, std, var
'''print(df.mean(numeric_only=True))
print(df.sum(numeric_only=True))
print(df.min(numeric_only=True))
print(df.max(numeric_only=True))
print(df.std(numeric_only=True))
print(df.var(numeric_only=True))
print(df.median(numeric_only=True))'''
#Aggregate on a specific column
'''print(df["Attack"].mean())
print(df["Defense"].sum())
print(df["HP"].min())
print(df["Speed"].max())
print(df["Sp. Atk"].std())
print(df["Sp. Def"].var())
print(df["Weight kg"].median())'''
#Aggregate on multiple columns
'''print(df[["Attack","Defense","HP"]].mean())
print(df[["Speed","Sp. Atk","Sp. Def"]].sum())
print(df[["Weight kg","Height m"]].min())
print(df[["Attack","Defense"]].max())
print(df[["HP","Speed"]].std())
print(df[["Sp. Atk","Sp. Def"]].var())
print(df[["Weight kg","Height m"]].median())'''
#Aggregate using groupby()
group=df.groupby("Type 1")
print(group["Attack"].mean())
print(group["Defense"].sum())
print(group["HP"].min())
