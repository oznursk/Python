import csv
with open("hafta_4/iris.data", newline="") as csvfile:
    reader= csv.DictReader(csvfile)
    for row in reader:
        print(row)
        print(row["species"])
  #sepal_lenth,sepal_width,petal_width,species