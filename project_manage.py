# import database module
import csv
from database import Table, Database

database = None
persons_table = None
login_table = None


# define a function called initializing
def initializing():
    # create an object to read all csv files that will serve as a persistent state for this program
    # create all the corresponding tables for those csv files
    # see the guide how many tables are needed
    # add all these tables to the database
    global database, persons_table, login_table
    database = Database()
    persons_table = Table('persons', 'persons.csv')
    login_table = Table('login', 'login.csv')
    database.insert(persons_table)
    database.insert(login_table)


# define a funcion called login
def login():
    # add code that performs a login task
    # ask a user for a username and password
    username = input('Username: ')
    password = input('Password: ')

    # returns [ID, role] if valid, otherwise returning None
    for user in database.search('login'):
        if user['username'] == username and user['password'] == password:
            return user['ID'], user['role']
    return None


# define a function called exit
def exit():
    with open('persons.csv', 'w', newline=''):
        persons_writer = csv.DictWriter('persons.csv', ['ID', 'fist', 'last', 'type'])
        persons_writer.writeheader()
        persons_writer.writerows(persons_table.table)
    with open('login.csv', 'w', newline=''):
        login_writer = csv.DictWriter('login.csv', ['ID', 'username', 'password', 'role'])
        login_writer.writeheader()
        login_writer.writerows(login_table.table)

    # write out all the tables that have been modified to the corresponding csv files
    # By now, you know how to read in a csv file and transform it into a list of dictionaries.
    # For this project, you also need to know how to do the reverse,
    # i.e., writing out to a csv file given a list of dictionaries.
    # See the link below for a tutorial on how to do this:
    # https://www.pythonforbeginners.com/basics/list-of-dictionaries-to-csv-in-python


# make calls to the initializing and login functions defined above

initializing()
val = login()

# based on the return value for login,
# activate the code that performs activities according to the role defined for that person_id

# if val[1] = 'admin':
    # see and do admin related activities
# elif val[1] = 'student':
    # see and do student related activities
# elif val[1] = 'member':
    # see and do member related activities
# elif val[1] = 'lead':
    # see and do lead related activities
# elif val[1] = 'faculty':
    # see and do faculty related activities
# elif val[1] = 'advisor':
    # see and do advisor related activities

# once everything is done, make a call to the exit function
exit()
