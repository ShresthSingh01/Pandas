import pandas as pd
'''data1={
    "Name":["Alice", "Bob", "Charlie", "David", "Eva"],
    "Age":[24, 27, 22, 32, 29]
}
df= pd.DataFrame(data1)
print(df)'''
# Accessing a specific row using loc
data={
    "Name":["Alice", "Bob", "Charlie", "David", "Eva"],
    "Age":[24, 27, 22, 32, 29]
}
df= pd.DataFrame(data,index=["emp1", "emp2", "emp3", "emp4", "emp5"])
print(df.loc["emp3"])
#Adding a new column to the DataFrame
df["Salary"]=[50000, 60000, 55000, 70000, 65000]
print(df)
#Adding a new row to the DataFrame
new_employee={"Name":"Frank", "Age":28, "Salary":62000}
df=pd.concat([df, pd.DataFrame([new_employee], index=["emp6"])])
print(df)