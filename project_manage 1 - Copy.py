from database import Database, Table
import csv


def initializing():
    db = Database()

    persons_table = Table("persons", "persons.csv")
    login_table = Table("login", "login.csv")
    grades_table = Table("grades", "grades.csv")

    db.insert(persons_table)
    db.insert(login_table)
    db.insert(grades_table)

    return db


session = initializing()


def login():
    username = input('Username: ')
    password = input('Password: ')
    for user in session.search('login').table:
        if user['username'] == username and user['password'] == password:
            return [user['ID'], user['role']]
    return None


def exit():
    for table in session.database:
        with open(table.directory, 'w', newline='') as file:
            fieldnames = table.table[0].keys() if table.table else []
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(table.table)


initializing()

val = login()
while val is None:
    val = login()


while val[1] == 'admin':
    while True:
        print("\nAdmin Menu:")
        print("1. Edit Database")
        print("2. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            while True:
                print("\nTables in Current session:")
                for i in range(len(session.database)):
                    print(f'{i+1}. {session.database[i].table_name}')

                edit_choice = int(input("Enter table to edit (0 to go back): "))

                if edit_choice == 0:
                    break
                else:
                    while True:
                        for j in range(len(session.database[edit_choice - 1].table)):
                            print(f"{j+1}. {session.database[edit_choice - 1].table[j]}")

                        index = int(input("Enter index to edit (0 to go back): "))
                        if index == 0:
                            break
                        else:
                            while True:
                                field = input("Enter field to edit (0 to go back): ")
                                if field == '0':
                                    break
                                else:
                                    new_value = input("Enter new value: ")
                                    session.database[edit_choice - 1].update(field, index-1, new_value)
                                    break
                            if field == '0':
                                break
                    if index == 0:
                        break
            if edit_choice == 0:
                continue

        elif choice == "2":
            print("\n")
            val = login()
            break


while val[1] == 'student':
    while True:
        invites = eval([user["invites"] for user in session.search("login").table if user["ID"] == val[0]][0])
        print("\nStudent Menu:")
        print("1. Create New Project")
        print(f"2. Check Invites ({len(invites)})")
        print("3. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter Project Title: ")
            username = [user["username"] for user in session.search("login").table if user["ID"] == val[0]][0]
            project = {"title": title, "user_ID": [val[0]], "project_ID": len(session.search('grades').table)+1,
                       "members": [username], "grade": "pending"}

            print(project)
            session.database[2].insert(project)
            print("Project created successfully.")

            for i, person in enumerate(session.search("persons").table):
                if person.get("ID") == val[0]:
                    session.database[0].update("type", i, "lead")

            for i, person in enumerate(session.search("login").table):
                if person.get("ID") == val[0]:
                    session.database[1].update("role", i, "lead")

            val[1] = 'lead'

            break

        elif choice == "2":
            while True:
                if invites:
                    for i in range(len(invites)):
                        print(f'{i+1}. {invites[i][0]} has invited you to their project.')

                        invite_choice = int(input("Choose number to respond (0 to go back): "))

                        if invite_choice == 0:
                            break
                        else:
                            respond_choice = input("Accept or Decline (a/d): ")
                            if respond_choice == 'a':
                                for j, person in enumerate(session.search("persons").table):
                                    if person.get("ID") == val[0]:
                                        session.database[0].update("type", j, "member")

                                for j, person in enumerate(session.search("login").table):
                                    if person.get("ID") == val[0]:
                                        session.database[1].update("role", j, "member")

                                val[1] = "member"
                                break

                            elif respond_choice == 'd':
                                for j, person in enumerate(session.search("login").table):
                                    if person.get("ID") == val[0]:
                                        invites.remove(invites[invite_choice - 1])
                                        session.database[1].update("invites", j, f"{invites}")
                        break
                else:
                    print("You have no invites.")
                    break

        elif choice == "3":
            print("\n")
            val = login()
            break

while val[1] == 'member':
    while True:
        print("\nMember Menu:")
        print("1. Edit Project")
        print("2. Invite Members")
        print("3. Leave Project")
        print("4. Logout")

        choice = input("Enter your choice: ")

        if choice == '1':
            while True:
                print("1. Edit Title")
                print("2. Submit project")
                print("3. Delete project")

                lead_choice = int(input("Enter your choice (0 to go back): "))

                if lead_choice == 0:
                    break

                elif lead_choice == 1:
                    print()
                    new_title = input("New Title: ")

                    for i, project in enumerate(session.search("grades").table):
                        if project.get("user_ID")[0] == val[0]:
                            session.database[2].update("title", i, new_title)
                            print(session.search("grades").table[i])
                            print("Changes saved")
                            print()

                elif lead_choice == 2:
                    pass

                elif lead_choice == 3:
                    for i, project in enumerate(session.search("grades").table):
                        if project.get("user_ID")[0] == val[0]:
                            del session.database[2].table[i]

                    for i, person in enumerate(session.search("persons").table):
                        if person.get("ID") == val[0]:
                            session.database[0].update("type", i, "student")

                    for i, user in enumerate(session.search("login").table):
                        if user.get("ID") == val[0]:
                            session.database[1].update("role", i, "student")

        if choice == "2":
            pass

        if choice == '4':
            print("\n")
            val = login()
            break

while val[1] == 'lead':
    while True:
        print("\nLead Menu:")
        print("1. Edit Project")
        print("2. Invite Members")
        print("3. Request Advisor")
        print("4. Logout")

        choice = input("Enter your choice: ")

        if choice == '1':
            while True:
                print("1. Edit Title")
                print("2. Submit project")
                print("3. Delete project")

                lead_choice = int(input("Enter your choice (0 to go back): "))

                if lead_choice == 0:
                    break

                elif lead_choice == 1:
                    print()
                    new_title = input("New Title: ")

                    for i, project in enumerate(session.search("grades").table):
                        if project.get("user_ID")[0] == val[0]:
                            session.database[2].update("title", i, new_title)
                            print(session.search("grades").table[i])
                            print("Changes saved")
                            print()

                elif lead_choice == 2:
                    pass

                elif lead_choice == 3:
                    for i, project in enumerate(session.search("grades").table):
                        if project.get("user_ID")[0] == val[0]:
                            del session.database[2].table[i]

                    for i, person in enumerate(session.search("persons").table):
                        if person.get("ID") == val[0]:
                            session.database[0].update("type", i, "student")

                    for i, user in enumerate(session.search("login").table):
                        if user.get("ID") == val[0]:
                            session.database[1].update("role", i, "student")

        elif choice == "2" or choice == "3":

            lead_username = [user["username"] for user in session.search("login").table if user["ID"] == val[0]][0]
            lead_project_ID = [project.get("project_ID") for project in session.database[2].table if project.get("user_ID")[0] == val[0]]

            if choice == "2":
                while True:
                    search_user = input("Username to invite: ")

                    students = [user['username'] for user in session.search('login').table if user['role'] == "student"]
                    matching_user = [username for username in students if username == search_user][0]

                    if matching_user:
                        for i, user in enumerate(session.search("login").table):
                            if user.get("username") == matching_user:

                                student_invites = eval(session.database[1].table[i]["invites"])
                                student_invites.append((lead_username, lead_project_ID))
                                session.database[1].update("invites", i, str(student_invites))

                                print("Invitation sent")
                                break
                    else:
                        print('Student not found')
                        break
                    break


            if choice == "3":
                while True:
                    search_user = input("Username to invite: ")

                    students = [user['username'] for user in session.search('login').table if user['role'] == "faculty"]
                    matching_user = [username for username in students if username == search_user][0]

                    if matching_user:
                        for i, user in enumerate(session.search("login").table):
                            if user.get("username") == matching_user:

                                student_invites = eval(session.database[1].table[i]["invites"])
                                student_invites.append((lead_username, lead_project_ID))
                                session.database[1].update("invites", i, str(student_invites))

                                print("Request sent")
                                break
                    else:
                        print('Faculty not found')
                        break
                    break

        elif choice == "4":
            print("\n")
            val = login()
            break

while val[1] == 'faculty':
    while True:
        invites = eval([user["invites"] for user in session.search("login").table if user["ID"] == val[0]][0])
        print("\nFaculty Menu:")
        print("1. See projects")
        print(f"2. Check Invites ({len(invites)})")
        print("3. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            while True:
                print("Current projects:")
                for i in range(len(session.search("grades").table)):
                    print(f"{i+1}. {session.search('grades').table[i]}")

                print()
                back = input("0 to go back: ")

                if back == "0":
                    break

        elif choice == "2":
            while True:
                if invites:
                    for i in range(len(invites)):
                        print(f'{i+1}. {invites[i][0]} has requested you to be their advisor.')

                        invite_choice = int(input("Choose number to respond (0 to go back): "))

                        if invite_choice == 0:
                            break
                        else:
                            respond_choice = input("Accept or Decline (a/d): ")
                            if respond_choice == 'a':
                                for j, person in enumerate(session.search("persons").table):
                                    if person.get("ID") == val[0]:
                                        session.database[0].update("type", j, "advisor")

                                for j, person in enumerate(session.search("login").table):
                                    if person.get("ID") == val[0]:
                                        session.database[1].update("role", j, "advisor")

                                val[1] = "advisor"
                                break

                            elif respond_choice == 'd':
                                for j, person in enumerate(session.search("login").table):
                                    if person.get("ID") == val[0]:
                                        invites.remove(invites[invite_choice - 1])
                                        session.database[1].update("invites", j, f"{invites}")
                            break
                    break
                else:
                    print("You have no invites.")
                    break

        elif choice == "3":
            print("\n")
            val = login()
            break

while val[1] == 'advisor':
    while True:
        print("\nAdvisor Menu:")
        print("1. See projects")
        print("2. Grade project")
        print("3. Add assistant")
        print("4. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            while True:
                print("Current projects:")
                for i in range(len(session.search("grades").table)):
                    print(f"{i+1}. {session.search('grades').table[i]}")

                print()
                back = input("0 to go back: ")

                if back == "0":
                    break

        if choice == "2":
            pass

        if choice == "3":
            pass

        if choice == "4":
            print("\n")
            val = login()
            break

# exit()
