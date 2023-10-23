import csv
from csv_tests.code_to_test import add_line
from csv_tests.code_to_test import remove_line


class TestCsv:
    def test_if_add(self):
        with open('file.csv', 'r') as f:
            reader = csv.reader(f)
            data = list(reader)
            row_count1 = len(data)
        add_line('file.csv', ['Rafa', 'Leao', 24, 'Male', 100000])
        with open('file.csv', 'r') as f:
            reader = csv.reader(f)
            data = list(reader)
            row_count2 = len(data)
        assert row_count2 > row_count1

    def test_if_remove(self):
        with open('file.csv', 'r') as f:
            reader = csv.reader(f)
            data = list(reader)
            row_count1 = len(data)
        remove_line('file.csv')
        with open('file.csv', 'r') as f:
            reader = csv.reader(f)
            data = list(reader)
            row_count2 = len(data)
        assert row_count2 < row_count1

