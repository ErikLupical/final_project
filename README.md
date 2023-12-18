# Project Repository

## Files in the Repo:

1. **persons.csv**
   - Contains information about persons.

2. **login.csv**
   - Contains users' login and project invite information.

3. **grades.csv**
   - Contains information about all projects.

4. **database.py**
   - Contains the classes used for the main project.

5. **project_manage.py**
   - Contains the program for senior project management.

6. **Readme.py**
   - Contains information about progress of the project.

7. **TODO.md**
   - Contains information on how the program is supposed to work.

8. **proposal.md**
   - Contains information on how the grading process is supposed to work.

## How to Compile and Run the Project:

open the project_manage.py file and run the program.

## Role-Based Access Control:

| Role          | Action                   | Methods  | Class | Completion Percentage |
|---------------|--------------------------|----------|-------|------------------------|
| Admin         | Update value field       | Update   | Table | 100%                   |
| Student       | Create new project       | Insert   | Table | 100%                   |
| Student       | Respond to invite        | Update   | Table | 70%                    |
| Lead/Member   | Edit Title               | Update   | Table | 100%                   |
| Lead          | Invite member            | Update   | Table | 80%                    |
| Lead          | Invite advisor           | Update   | Table | 80%                    |
| Member        | Leave project            | Update   | Table | 0%                     |
| Faculty       | Respond to invite        | Update   | Table | 70%                    |
| Advisor/Faculty| See all projects         | Search   | Table | 100%                   |
| Advisor/Faculty| Grade Project            | Update   | Table | 0%                     |
| Advisor       | Add assistant            | Update   | Table | 0%                     |

## Features Yet to be Implemented:

- Grading system for advisor and faculty.
- Adding assistant.
- Members inviting more members.
- Members leaving the project.

## Known Bugs:

1. Users are able to send invites to themselves.
2. When a student sends an invite to another student, log out, and the student that the invite was sent to tries to log in, the program ends.
3. When faculty accepts a request, they do not become an advisor (this may extend to students as well).
4. Logging out has several issues.