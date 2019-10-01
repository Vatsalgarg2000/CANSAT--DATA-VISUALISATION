import csv
import random
import time

x_value = 0
first_column = 1000
second_column = 1000
third_column = 1000 
fourth_column = 1000
fifth_column = 1000
sixth_column = 1000
seventh_column = 1000 
eight_column = 1000

fieldnames = ["x_value", "first_column", "second_column","third_column","fourth_column","fifth_column",
              "sixth_column","seventh_column","eight_column"]


with open('data.csv', 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()

while True :

    with open('data.csv', 'a') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        info = {
            "x_value": x_value,
            "first_column": first_column,
            "second_column": second_column,
            "third_column": third_column,
            "fourth_column": fourth_column,
            "fifth_column": fifth_column,
            "sixth_column": sixth_column,
            "seventh_column": seventh_column,
            "eight_column": eight_column
        }

        csv_writer.writerow(info)
        print(x_value, first_column, second_column,third_column,fourth_column,fifth_column,sixth_column
              ,seventh_column,eight_column)

        x_value += 1
        first_column = first_column + random.randint(-15,15)
        second_column = second_column + random.randint(-5, 16)
        third_column = third_column + random.randint(-16,10)
        fourth_column = fourth_column + random.randint(-9,6)
        fifth_column = fifth_column + random.randint(-14,10)
        sixth_column = sixth_column + random.randint(-5, 6)
        seventh_column = seventh_column + random.randint(-6,10)
        eight_column = eight_column + random.randint(-12,16)

    time.sleep(1)