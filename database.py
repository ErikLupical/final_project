# try wrapping the code below that reads a persons.csv file in a class
# and make it more general such that it can read in any csv file

import csv
import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

persons = []
with open(os.path.join(__location__, 'persons.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        persons.append(dict(r))
print(persons)


# add in code for a Database class
class Database:
    def __init__(self):
        self.database = []

    def insert(self, table):
        self.database.append(table)

    def search(self, table_name):
        for table in self.database:
            if table.table_name == table_name:
                return table

# add in code for a Table class
class Table:
    def __init__(self, table_name, directory):
        self.table_name = table_name
        self.table = []
        with open(directory,'r') as file:
            table_reader = csv.DictReader(file)
            for row in table_reader:
                self.table.append(row)

    # modify the code in the Table class so that it supports the insert operation
    # where an entry can be added to a list of dictionary
    def insert(self, new_row):
        self.table.append(new_row)

    # modify the code in the Table class so that it supports the update operation
    # where an entry's value associated with a key can be updated
    def update(self, key, value, new_value):
        for row in self.table:
            if row.get(key) == value:
                row[key] = new_value

    def __str__(self):
        return self.table_name + ':' + str(self.table)

test = Table('test', 'persons.csv')
print(test.table)
