import csv
with open("demo.csv","r") as p:
    empdata=csv.reader(p)
    for r in empdata:
        print(r)
