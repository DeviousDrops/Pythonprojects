import pandas
data=pandas.read_csv("sqdata.csv")
count=len(data[data["Primary Fur Color"] == "Gray"])
print("no. of gray squirrels =",count)
