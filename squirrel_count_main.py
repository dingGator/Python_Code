# how many black, grey, red # "Primary Fur Color"

import pandas

# data = pandas.read_csv("weather_data.csv")
# print(data)
# print(data["temp"])
grey_total = 0
black_total = 0
cinnamon_total = 0
test_total = 0

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
temp_list = data["Primary Fur Color"].to_list()
#print(f" temp_list:  {temp_list}")

for color in temp_list:
    if color == "Gray":
        grey_total += 1
    elif color == "Black":
        black_total += 1
    elif color == "Cinnamon":
        cinnamon_total += 1

print(f"0,gray,{grey_total} \n1,black,{black_total}\n2,cinnamon,{cinnamon_total}")

black_count = len(data[data["Primary Fur Color"] == "Black"])
grey_count = len(data[data["Primary Fur Color"] == "Gray"])
red_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
print(black_count)
print(grey_count)
print(red_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_count, red_count, black_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")

