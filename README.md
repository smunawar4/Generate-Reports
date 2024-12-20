# Fall 2024 Assignment 2
Overview: User Reports and Management 
________________________________________________________________________________

Project Description: 
Seneca has hired us to write a report on current and future student enrollments, 
to see what programs they enroll in, what electives they enroll into, etc.  
This will allow them to decide their budget. 
The problem is that there are many students and writing the report manually 
would be very tedious so we want to automate a script that will generate a 
report organized however we want.
________________________________________________________________________________

User Reports: 
Files that contain information by future and current students.

Examples of Reports Generated: 
	Dietary (Vegetarians Y or N/ Halal/ Allergies)
	Transportation (Car, Bus, Special Seneca shuttle)
	Electives 
	First Name and Last Names

Management: 
A function that will categorize the data of the user reports based on similarities 
in the information such as programs and teachers. 

________________________________________________________________________________

Schema:
FIRST_NAME, LAST_NAME, STUDENT_ID, PROGRAM NAME, ELECTIVE, DIETARY, TRANSPORTATION

________________________________________________________________________________

Questions:

How will your program gather required input?
	The program open a plaintext file that contains student information 
	unorganized. It will then manage the information organize it based on 
	user input.

How will your program accomplish its requirements? 
	Iteration like for and while loops, if statements to determine how the 
	reports should be organized 
	Functions used: 'user_report', 'management'
	Using linux commands like head to show a preview, so we will use imports 
	like os and subprocess.

How will output be presented? 
	The program will generate a report based on how the user has chosen to 
	generate it. All reports will be given unique names as users can 
	generate multiple of them.

What arguments or options will be included? 
	How the user would like to organize the report.
	If the user would like a preview of the report (first 5 lines)

What aspects of development do you think will present the most challenge?
	Making sure the reports are organized in the manner that the user chose
	If there are duplicate student information in the report, how to get 
	the program to only write a student's name once.

________________________________________________________________________________

PseudoCode:

Start 
Check if the folder School Report exist. If not, create it.
Ask the user to input a report name
If the user has submitted no file, or a file that does not exist, print an error message and go to Step 3.
If the file exist, go to step 4
Ask the user how they would like to organize the file:
Alphabetically?
Based on Courses/Electives
Based on Programs
Dietary
Transportation 
Organize the file based on User Input
Prompt user for either submitting the report or not: Y or N
If User entered Y , go to step 5
If User entered N, go to step 4
Create the report.
Ask User if they would like to preview the report
If Y, print the first 5 lines
If N, move to step 9
Move the file to 'SchoolReport'.
End
