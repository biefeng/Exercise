import csv

with open("test.csv", mode="w",newline="\n") as t:
    writer = csv.writer(t, delimiter=",")
    writer.writerows([["Hi","HA"]*5]*3 )


with open("test.csv",mode="r",newline="\n") as t:
    reader = csv.reader(t, delimiter=",")
    for row in reader:
        print(type(row))
        row.append("Hello")
        print(row)
