import pandas as pd

#read the files
df = pd.read_csv("spain_province.csv", sep =";")
df2 = pd.read_excel("report.xlsx")

#create mapping dictionary town -> province
mapping = df[['Official Name Municipality', 'Official Name Province']].drop_duplicates()
town_to_province = dict(zip(mapping['Official Name Municipality'], mapping['Official Name Province']))

#append values from dictionary
df2["Province"] = df2["Town"].map(town_to_province)

df2.to_excel("report.xlsx", index=False)

print(town_to_province)