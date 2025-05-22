# Instruction

## First Instruction
Ask the user to enter a username and a password.

### Authorization
Validate if the username and password match preset values (e.g., "admin" and "1234").

## Second Instruction
If login is successful:

Ask for the user's role (e.g., "student" or "teacher").

## Third Instruction
If the user is a "teacher":
### Teacher Output
Ask how many students are in class.

Print: "Welcome, teacher. You are managing [n] students."

### Student Output
If the user is a "student":

Ask what subject they like.

Print: "Hello student! Enjoy studying [subject]."

## Unknown Role Output
If the role is something else, print: "Unknown role. Access limited."
## Login Fail
If login fails, print: "Incorrect username or password."
