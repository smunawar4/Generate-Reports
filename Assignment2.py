#!/usr/bin/env python3
# Project Name: Assignment 2
# Group 3
# Student Name: Saira Munawar, Andrew, Juliana, Nishan, Shawmya Sivakumar

import sys, os, datetime, shutil

def school_folder(folder_path):
	'''Creates the school folder if it does not exit.'''
	if os.path.isdir(folder_path): #using os.dir to find school_folder in the a2assignment
		return folder_path + ' exists'
	else:
		os.mkdir(folder_path) #creates the folder otherwise
		return folder_path + ' has been created.'

def usage():
	'''prints messages to users'''
	if len(sys.argv) != 3:
		print('USAGE: ' + sys.argv[0] + ' File_Name' + ' Options') #if the user does not use 3 arguments: filename + options + program name
		sys.exit() 
	else:
		file_name = sys.argv[1] 
		option = sys.argv[2]
		management(file_name, option) #call the management function

def read_text_file(file_name):
	'''opens the file given by the user'''
	if os.path.isfile(file_name): #checks if the file is found
		return 'File found!'
	else:
		print('File not found')
		sys.exit()

def management(file_name, option):
	'''This function organizes the file based on the user's input'''
	'''Options are: alphabetical, dietary, transportation, program name, elective, campus'''
	file_content = read_text_file(file_name) #checks if the file exist
	print(file_content) 
	print('option:', sys.argv[2])

	if option.lower() == 'a' or option.lower() == 'alphabetical':
		alp_order(file_name)

	elif option.lower() == 'p' or option.lower() == 'program':
		program_name(file_name)

	elif option.lower() == 'e' or option.lower() == 'elective':
		elective(file_name)

	elif option.lower() == 'c' or option.lower() == 'campus':
		campus(file_name)

	elif option.lower() == 't' or option.lower() == 'transportation':
		transportation(file_name)

	elif option.lower() == 'd' or option.lower() == 'dietary':
		dietary(file_name)

	elif option.lower() == 's' or option.lower() == 'student':
		find_student(file_name)
	else:
		print('Please enter an option (Alphabetical (a), Program (p), Elective (e)\nCampus (c), Transportation (t), Dietary (d), Student (s)')

def alp_order(file_name):
	'''Function will sort the list alphabetically.'''
	option = 'Alphabetical' #for generate_report

	f = open(file_name, 'r') # Opens the file in read mode
	lines = f.readlines() # Read all the lines from the file'

	students = [] # Creating a list to store student data
	dup_ids = set() #create a set to store non duplicate ids

	for line in lines:
		name_split = line.strip().split(',') # Split the line by commas
		if len(name_split) < 8: #checks that line has at least 8 elements after splitting
			print(f"Invalid line: {line.strip()}")
		else:
			first_name = name_split[0] # Extracting the full name
			last_name = name_split[1]
			student_id = name_split[3] # extracting the student_id
			name_format = f"{last_name} {first_name}" # To change the name format as lastname firstname

			if len(name_split) > 1 and student_id not in dup_ids: 
				students.append((last_name, name_format)) # Append it to the list student
				dup_ids.add(student_id)

	f.close()
	students.sort() # Sorts the name by lastname of the students in alphabetical order
	generate_report(option, [student[1] for student in students])  

def program_name(file_name):
	'''Function will ask user to input a program and pull a list of all users and total users in that program'''
	option = 'Program'

	file = open(file_name, 'r')    

	enrolled_programs = [] #stores valid entries as tuples
	program_report = []
	dup_ids = set() #will store the student ids - ensures non duplicate data.

	for line in file: #iterate over each line in the file
		students_data = [item.strip().strip("'") for item in line.split(',')] #removes any whitespace from the line, any surrounding single quotes, splits line into components

		program = students_data[4] #fifth field 
		first_name = students_data[0] #first field
		last_name = students_data[1] #second field
		student_id = students_data[3] #forth field

		student_name = f"{first_name} {last_name}" #combines first and last name
		
		if len(students_data) < 8: #checks that line has at least 8 elements after splitting
			print(f"Invalid line: {line.strip()}") #if line doesn't meet criteria, print message tells us its being skipped
		else:
			if student_id not in dup_ids: #ensures that there are no duplicates
				enrolled_programs.append((student_name, program)) #creates a tuple, and adds it to the list enrolled_programs. Now all valid entries from the file are stored.
				dup_ids.add(student_id) #add the student ids to the set. Ensures that data is not duplicates.
	
	#Close the file after reading it
	file.close()

	#Ask the user which program their looking for
	searched_program = input("Enter the program name you are looking for: ").strip() #removes leading or trailing whitespace from input

	#Find all the students enrolled in that program, loops through each tuple in enrolled_programs, compares program with searched program, collects names of the students enrolled in the matching program
	enrolled_in_program = [student for student, program in enrolled_programs if program.lower() == searched_program.lower()]
	count = len(enrolled_in_program) #counts how many students are in that program
	
	#print the results of the search
	if enrolled_in_program:
		print(f"Students enrolled in {searched_program}:")
		for student in enrolled_in_program: #loops through each student in list of matches, and prints each
			program_report.append(student) #adds it to the report
	else:
		program_report.append(f"There are no students found in the program: {searched_program}") #adds it to the report

	program_summary = (f"{searched_program} - {count} occurance(s)") 
	program_report.append(program_summary)
	generate_report(option, program_report)

def elective(file_name):
	'''Function will ask user to input an elective and pull a list of all users and total users in that program'''
	option = 'Elective'

	#Open and read the file with student and elective data
	file = open(file_name, 'r')

	enrolled_electives = []
	elective_report = []
	dup_ids = set()

	for line in file: #iterate over each line in the 
		students_electives = [item.strip().strip("'") for item in line.split(',')] #removes any whitespace from the line, any surrounding single quotes, splits line into components
		
		elective = students_electives[5] #six field
		first_name = students_electives[0]
		last_name = students_electives[1]
		student_id = students_electives[3] #forth field

		full_name = first_name + ' ' + last_name #combines first and last name

		if len(students_electives) < 8: #checks that line has at least 8 elements after splitting
			print(f"Skipping invalid line: {line.strip()}") #if line doesn't contain 8 items, print message tells us its being skipped
		else:
			if student_id not in dup_ids: #ensures duplicate data is not added
				enrolled_electives.append((full_name.strip(), elective.strip())) #creates a tuple, and adds it to the list enrolled_electives. Now all valid entries from the file are stored.
				dup_ids.add(student_id) #adds student id to set

	#Close the file after reading it
	file.close()

	#Ask the user which program their looking for
	searched_elective = input("Enter the Elective name you are looking for: ").strip()

	#Find all the students enrolled in that program
	enrolled_in_elective = [student for student, program in enrolled_electives if program.lower() == searched_elective.lower()]
	count = len(enrolled_in_elective) #count how many students are in the electives

	#print the results of the search
	if enrolled_in_elective:
		print(f"Students enrolled in {searched_elective}:")
		for student in enrolled_in_elective:
			elective_report.append(student)
	else:
		elective_report.append(f"There are no students found in the electives: {searched_elective}")

	program_summary = (f"{searched_elective} - {count} occurance(s)")
	elective_report.append(program_summary)
	generate_report(option, elective_report)


def campus(file_name): 
	'''User will enter a campus and the program will display the campus and the users'''
	option = 'Campus'
	filename = 'campus.txt'
	
	#ask user to search for file
	campus_search = input('Enter the Campus: (York, Markham, Newnham, King): ').strip().lower()
	if campus_search not in ['york', 'markham', 'newnham', 'king']:
		print('Invalid Entry. Must be York, Markham, Newnham or King')
		sys.exit()

	with open(filename, 'r') as file:
		seneca_details = []
		# Process each line in the file
		campus_data = file.readlines()
		seneca_campuses = [campus_name.strip() for campus_name in campus_data]
		for campus_name in seneca_campuses:
			if campus_search in campus_name.lower(): 
				seneca_details = [f"Details for {campus_search.capitalize()} campus: {campus_name}"]

	with open(file_name, "r") as file:
		data = file.readlines()  # Read all lines from the file
		campus_details = set()
		for line in data:
			campus_comp = [comp.strip(" '") for comp in line.strip().split(",")]  # Clean up each component
			campus = campus_comp[2]  # campus mode is the 3rd field

			if len(campus_comp) < 8:  # Ensure there are enough fields
				print(f"Invalid line: {line.strip()}") #skip the line and print a message informing the user

			if campus.lower() == campus_search: 
				campus_info_str = ", ".join(campus_comp)
				campus_details.add(campus_info_str) 
			else:
				campus_report = [f"There are 0 students at: {campus_search}"]

		unique_count = len(campus_details)
		campus_summary = [f"{campus_search} - {unique_count} occurrence(s)"]
		campus_report = seneca_details + list(campus_details) + campus_summary

		generate_report(option, campus_report)

def transportation(file_name):
	''' Reads the file 'user_test' and returns a summary of transportation preferences'''
	option = 'Transportation'

	with open(file_name, "r") as file:
		data = file.readlines()  # Read all lines from the file

		# Initialize an empty dictionary to store dietary preference counts
		transport_preferences = {}
		unique_transport_entries = set()

		transport_search = input('Enter the diet: (Car, Bus, Shuttle, Train: ').strip().lower()
		if transport_search  not in ['car', 'bus', 'shuttle', 'train']:
			print('Invalid Entry. Must be Car, Bus, Shuttle or Train')
			sys.exit()

		# Process each line in the file
		for line in data:
			components = [comp.strip(" '") for comp in line.strip().split(",")]  # Clean up each component
			if len(components) < 8:  # Ensure there are enough fields
				print(f"Invalid line: {line.strip()}")
				continue  # Skip invalid lines with insufficient data
			
			transport = components[7]  # Dietary preference is the 7th field

			if transport.lower() == transport_search :
				transport_details_str = ", ".join(components)
				unique_transport_entries.add(transport_details_str)
				# Count occurrences of each dietary preference
				transport_preferences[transport] = transport_preferences.get(transport, 0) + 1
			else:
				transport_report = [f"There are 0 occurence of {transport_search}"]

		unique_count = len(unique_transport_entries) 
		transport_summary = [f"{diet} - {unique_count} occurrence(s)" for diet in transport_preferences.keys()]
		transport_report = list(unique_transport_entries) + transport_summary
		generate_report(option, transport_report)

def dietary(file_name):
	'''Reads the file 'user_test' and returns a summary of transportation preferences'''
	option = 'Dietary'

	with open(file_name, "r") as file:
		data = file.readlines()  # Read all lines from the file

		# Initialize an empty dictionary to store dietary preference counts
		dietary_preferences = {}
		unique_dietary_entries = set()

		dietary_search = input('Enter the diet: (Vegetarian, Vegan, Halal, N/A: ').strip().lower()
		if dietary_search not in ['vegetarian', 'vegan', 'halal', 'n/a']:
			print('Invalid Entry. Must be Vegetarian, Vegan, Halal or N/A')
			sys.exit()

		# Process each line in the file
		for line in data:
			components = [comp.strip(" '") for comp in line.strip().split(",")]  # Clean up each component
			if len(components) < 8:  # Ensure there are enough fields
				continue  # Skip invalid lines with insufficient data
			
			diet = components[6]  # Dietary preference is the 7th field

			if diet.lower() == dietary_search:
				dietary_details_str = ", ".join(components)
				unique_dietary_entries.add(dietary_details_str)
				# Count occurrences of each dietary preference
				dietary_preferences[diet] = dietary_preferences.get(diet, 0) + 1
			else:
				dietary_report = [f"There are 0 occurence of {dietary_search}"]

		unique_count = len(unique_dietary_entries) 
		dietary_summary = [f"{diet} - {unique_count} occurrence(s)" for diet in dietary_preferences.keys()]
		dietary_report = list(unique_dietary_entries) + dietary_summary
		generate_report(option, dietary_report)

def find_student(file_name):
	'''user will input name and student_id and find the the user'''
	option = 'Student'
	f = open(file_name, 'r') # Open the file in read mode
	lines = f.readlines() # read all the lines from the provided file.
	f.close()
	search_student = input('Enter the student name or ID: ').strip().lower() # Prompts the user for input to search for specific student.
	found_students = [] #stores the found students
	
	for line in lines:
		student_info = line.strip() 
		if search_student in line.lower() and student_info not in found_students: #checks if searched student is in file and if it is not a duplicate
			found_students.append(student_info) #adds the student information to found_students
	if not found_students:
		found_students.append(f"There are no students with that name: {search_student}")

	generate_report(option, found_students)
  
def generate_report(option: str, information: list):
	'''Takes the management report and generates it into a file and moves it to the school folder'''

	current_date = datetime.datetime.now()
	formatted_date = current_date.strftime('%d-%m-%Y-%H-%M-%d')
	filename = "Report_" + option + "_" + formatted_date + ".txt"
	print('file generated will be named: ' + filename)

	f = open(filename, "a")
	f.write(option + " Report\n")
	f.write("=" * 80 + "\n")
	
	if information:
		for info in information:
			f.write(info + "\n")
	else:
		f.write("No " + option + " found matching your query.\n")

	f.close()
	print('Report was generated: ' + filename)

	source = filename
	destination = 'school_folder'
	try:
		dest = shutil.move(source, destination) 
	except shutil.Error:
		return 'File with that name exists already. Please try again in a minute.'

if __name__ == '__main__':
	folder_path = 'school_folder' #the path of the folder - should be in the same directory as assignment 2
	print(school_folder(folder_path))
	usage()
