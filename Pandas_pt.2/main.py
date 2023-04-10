import pandas

# Importing Data from CSV file
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

x = data["Primary Fur Color"].value_counts()
print(x)

# Dictionary to help format data
data_dict ={
    'Fur Color': ['Gray', 'Cinnamon', 'Black'],
    'Count of Color': [2473, 392, 103]
}
# Create an Excel CSV file with new data captured
data = pandas.DataFrame(data_dict)
data.to_csv("Count_Color")
print(data_dict)

