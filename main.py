import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrel = data[data["Primary Fur Color"] == "Gray"]
red_squirrel = data[data["Primary Fur Color"] == "Cinnamon"]
black_squirrel = data[data["Primary Fur Color"] == "Black"]
gray_count = 0
red_count = 0
black_count = 0
for squirrel in gray_squirrel["X"]:
    gray_count += 1
for squirrel in red_squirrel["X"]:
    red_count += 1
for squirrel in black_squirrel["X"]:
    black_count += 1
number_of_squirrels = \
    {
        "fur color": ["gray", "red", "black"],
        "Count": [gray_count, red_count, black_count],
    }
new_data = pandas.DataFrame(number_of_squirrels)
new_data.to_csv("new_data.csv")


