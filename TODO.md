# Project Management System

## Roles and Actions:

### Admin
- Can edit each value of each entry of each table in the database.

### Student
- Can create a new project. The new project is added to the "grades" table with their username and ID set as the project's lead.
- **Respond to Invites:**
  - If the student accepts the invite, they become a member, and their username and ID are added to the members list of the project they are invited to (indicated by the second value of the invite tuple).
  - If the student declines the invite, the invite tuple is removed from their invites list.

### Lead
- Can edit the name of the project they are leading.
- Submitting the project allows the advisor (and their assistants) to grade the project.
- Send invites to other students by adding an invite tuple to their invite list.
- Send a request to faculty by adding an invite tuple to their invite list.

### Member
- Can edit the name of the project they are leading.
- Send invites to other students by adding an invite tuple to their invite list.
- Submitting the project allows the advisor (and their assistants) to grade the project.
- Can leave the project; removes the invite tuple associated with their project and changes the role from member to student. Their username and ID are also removed from project members and user_ID lists.

### Faculty
- Can see all projects present.
- **Respond to Invites:**
  - If the faculty accepts the invite, they become an advisor and can see the information about the project they are invited to (indicated by the second value of the invite tuple).
  - If the faculty declines the invite, the invite tuple is removed from their invites list.

### Advisor
- Can see all projects present.
- Can grade a project by updating the grade field associated with the project from pending to the grade the advisor has given.
- Can invite other faculty to be an assistant, in which case they are also able to update the grade of the project.
