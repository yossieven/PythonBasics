import os
import pandas
import time

while True:
    if os.path.exists("files/temps_today.csv"):
        data = pandas.read_csv("files/temps_today.csv")
        print(data.mean())
    else:
        print("file doesn't exist")

    time.sleep(5)




