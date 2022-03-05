import csv

# 216
#with open("data.csv") as data_file:
#    data = data_file.readlines()
#    print(data)

# extract ids from data
#with open("data.csv") as data_file:
#    data = csv.reader(data_file)
#    ids = []
#    for row in data:
#        identification_num = row[1]
#        if identification_num.isnumeric():
#            ids.append(int(identification_num))

# alternative: using pandas
import pandas
#data = pandas.read_csv("data.csv")
# print(data)
# print(data["Nutzername"])

# 217
# print(type(data)) # = DateFrame
# print(type(data["Nutzername"])) ' = Series

# create dictionaries
#data_dict = data.to_dict()

# create python LIST
#id_list = data["Identifikation"].to_list()
# create AVERAGE
#avg = sum(id_list) / len(id_list)
#avg = data["Identifikation"].mean()
# find MAX
#max = data["Identifikation"].max()
#max = data.Identifikation.max()

# get data in ROW
#row = data[data.Nutzername == "booker12"]
# get row with MAXIMUM value
#row = data[data.Identifikation == data.Identifikation.max()]
# get Mary's ID
#mary = data[data.Vorname == "Mary"]
#mary_id = int(mary.Identifikation)

# create a dataframe
#data_dict = {
#    "students": ["Amy", "James", "Angela"],
#    "scores": [76, 56, 65]
#}
#data = pandas.DataFrame(data_dict)
#data.to_csv("new_data.csv")

# 228
# extact squirrel counts
data = pandas.read_csv("squirrel_count.csv")
colors = data["Primary Fur Color"]
occurrence = colors.value_counts()
data_dict = {
    "Primary Fur Color": [occurrence.index[0], occurrence.index[1], occurrence.index[2]],
    "Counts": [occurrence.values[0], occurrence.values[1], occurrence.values[2]]
}
df = pandas.DataFrame(data_dict)
df.to_csv("count_data.csv")

