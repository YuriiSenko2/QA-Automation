import csv
import pandas as pd


def add_line(file_name, listing):
    with open(file_name, 'a', newline='') as csvf:
        file_writer = csv.writer(csvf, delimiter=',')
        file_writer.writerow(listing)


def remove_line(filename):
    df = pd.read_csv(filename)
    df.drop(df.tail(1).index, inplace=True)
    df.to_csv(filename, index=False)


