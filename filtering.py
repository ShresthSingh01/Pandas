#filtering = keeping the rows that meet a certain condition
import pandas as pd
df = pd.read_csv("Pokemon.csv")
#filtering based on a single condition
'''fire_type = df[df["Type 1"]=="Fire"]
print(fire_type.to_string())
tall_pokemon = df[df["Height m"]>2]
print(tall_pokemon.to_string())
water_pokemon = df[df["Type 1"]=="Water"]
print(water_pokemon.to_string())'''
#filtering based on multiple conditions
ff_pokemon = df[(df["Type 1"]=="Fire") & (df["Type 2"]=="Flying")]
print(ff_pokemon.to_string())
ht_pokemon = df[(df["Height m"]>2) | (df["Weight kg"]>200)]
print(ht_pokemon.to_string())
#negating a condition   
not_grass = df[~(df["Type 1"]=="Grass")]
print(not_grass.to_string())