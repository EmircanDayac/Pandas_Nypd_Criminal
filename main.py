

list_gray_sincup_Gray = []
list_gray_sincup_Cinnamon = []
list_gray_sincup_Black = []

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
data2 = data["Primary_Fur_Color"]
for i in data2:
    if i == "Gray":
        list_gray_sincup_Gray.append(i)

for i in data2:
    if i == "Cinnamon":
        list_gray_sincup_Cinnamon.append(i)

for i in data2:
    if i == "Black":
        list_gray_sincup_Black.append(i)

data_dict = {
    "Colour": ["gray", "Cinnamon", "Black"],
    "Count": [len(list_gray_sincup_Gray), len(list_gray_sincup_Cinnamon), len(list_gray_sincup_Black)]
}
_pandas = pandas.DataFrame(data_dict)
_pandas.to_csv("Sincap")

print(data2)
