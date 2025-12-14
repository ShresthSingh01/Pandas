import pandas as pd
data1=["a", "b", "c", "d", "e"]
p= pd.Series(data1)
print(p)
data=[100, 200, 300, 400, 500]
s = pd.Series(data,index=["a", "b", "c", "d", "e"])
# Adding a new value to the Series
s.loc["a"] = 1000
print(s)
print(s.loc["c"])
#new 
calories={"day1": 420, "day2": 380, "day3": 390, "day4": 410}
series= pd.Series(calories)
series.loc["day1"] +=  450  # Updating the value for day1
print(series)
print(series[series > 400])  # Filtering values greater than 400


