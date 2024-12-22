# # with open("weather_data.csv") as data_files:
# #     data = data_files.readlines()
# #     print(data)
#
# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         # print(row)
#         ## To get only temperature values
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     # print(temperatures)
#
# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# # print(data["temp"])
#
# temp_list = data["temp"].to_list()
# # print(len(temp_list))
#
# ## average of temp
# avg_temp = sum(temp_list) / len(data["temp"])
# # print(avg_temp)
# # print(data["temp"].mean())
# # print(data["temp"].max())
#
# ## Get Data in Column
# # print(data["condition"])
# # print(data.condition)
#
# ## Get Data in Row
# # print(data[data.day == "Monday"])
# # print max temp row
# # print(data[data.temp == data.temp.max()])
#
# # get mondays temp
# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0] * (9 / 5) + 32
# # print(monday_temp)
#
# ## Create dataframe from scratch
# data_dict = {
#     "students": ["Devji", "Senpai", "Sru", "Sii"],
#     "scores": [70, 64, 62, 53]
# }
# data1 = pandas.DataFrame(data_dict)
# print(data1)
# data1.to_csv("new_data.csv")


import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
# print(grey_squirrels_count)
# print(cinnamon_squirrels_count)
# print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrrel_count.csv")
