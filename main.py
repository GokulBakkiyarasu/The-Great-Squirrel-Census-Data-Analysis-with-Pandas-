import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_count = len(data[data["Primary Fur Color"] == "Gray"])
red_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_count = len(data[data["Primary Fur Color"] == "Black"])
number_of_squirrels = {
        "fur color": ["gray", "red", "black"],
        "Count": [gray_count, red_count, black_count],
    }
new_data = pandas.DataFrame(number_of_squirrels)
new_data.to_csv("new_data.csv")

