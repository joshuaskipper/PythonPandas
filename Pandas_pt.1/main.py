# # How to open csv file and turn it into a list.
with open('weather_data.csv') as data_file:
    data = data_file.readlines()
    print(data)

# How to open csv file in a data format
# import csv
#
# with open('weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for i in data:
#         print(i)
#         # Grabs only the Tempature from the days of the week
#         if i[1] != "temp":
#             temperatures.append(int(i[1]))
# print(temperatures)


# Using Pandas
import pandas

# Data.frame(Whole table) vs Data.Series(Row of table)
data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(data)
# print(type(data['temp']))
# print(data['temp'])

data_dict = data.to_dict()
print(data_dict)

# Getting the mean max min
temp_list = data["temp"].to_list()
print(temp_list)
x = 0
count = 0
for i in temp_list:
    count += 1
    x += i

print(count)
print(x)
avg_temp = x / 7
print(avg_temp)

print(data['temp'].max())
print(data['temp'].mean())
print(data['temp'].min())

# Get Data in columns
# print(data['condition'])
# print(data.condition)

# Get Data in Row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
#
# fahrenheit = ((monday.temp * 9/5) + 32 )
# print(fahrenheit)


# #Create a dataframe from scratch
# data_dict = {
#     "student": ['Josh', 'dez', 'mom', 'Josh', 'Josh', 'Josh', 'dez', 'dez', 'mom', ],
#     "grades": [77, 55, 88]
# }
# #Create a count of unique values
# data = pandas.DataFrame(data_dict)
# data["Josh"].value_counts()
#
# #Create a csv file
# data.to_csv("new_data.csv")
# print(data)
#
# print(data_dict)
