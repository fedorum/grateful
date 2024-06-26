import os
import datetime
import random

# initialises the current date and file to store 'grateful' entries
today = datetime.date.today().strftime("%d %B %Y")
file = 'grateful.txt'

# prints a welcome message and a random entry (if existing)
print("Welcome to Grateful!")
with open(file, 'r') as g:
    lines = g.readlines()
    index = len(lines)
if lines:
    print("\nHere's something you were grateful for on\n")
    print(random.choice(lines).strip("\n"))

# runs a loop until the user ends the program
while True:
    command = input("\nWhat would you like to do? (entry/ view/ delete/ edit/ exit) ").lower()

    # allows user to enter an entry
    if command == "entry":
        entry = input("\nWhat do you feel grateful about today? ")
        while entry <= "":
            print("\nThat's not a valid entry :(")
            entry = input("Please input a valid entry or 'return' if you would like to go back: ")
        if entry.lower() == "return":
            continue

        with open(file, 'a') as g:
            index += 1
            g.write("{}. {}: {}\n".format(index, str(today), str(entry)))
        print('\n' + "New entry created!")

    # displays all recorded entries
    elif command == "view":
        with open(file, 'r') as g:
            lines = g.readlines()
        if not lines:
            print("\nOh no! You haven't added any entries yet...")
        else:
            print("\nHere's everything you've ever been grateful for!")
            with open(file, 'r') as g:
                print(g.read().strip("\n"))

    # allows the user to remove a previously recorded entry
    elif command == "delete":
        delete = input("\nInput the index of the entry you would like to delete (i.e. 5): ")
        while True:
            flag = True
            try:
                int(delete)
            except ValueError:
                flag = False
            if delete <= "" or not delete.isdigit() or not flag:
                print("\nThat's not a valid index :(")
                delete = input("Please input a valid index or 'return' if you would like to go back: ")
            elif flag:
                if int(delete) > index:
                    print("\nThat's not a valid index :(")
                    delete = input("Please input a valid index or 'return' if you would like to go back: ")
                else:
                    break
            elif delete.lower() == "return":
                continue

        with open(file, 'r') as infile, open("temp.txt", 'w') as outfile:
            i = 1
            for line in infile:
                if delete + "." not in line:
                    outfile.write("{}.".format(i) + line[2:])
                    i += 1
        os.replace('temp.txt', file)
        print("\nSuccessfully deleted a record!")

    # allows the user to edit a previously recorded entry
    elif command == "edit":
        edit = input("\nInput the index of the entry you would like to edit (i.e. 5): ")
        while True:
            flag = True
            try:
                int(edit)
            except ValueError:
                flag = False
            if edit <= "" or not edit.isdigit() or not flag:
                print("\nThat's not a valid index :(")
                edit = input("Please input a valid index or 'return' if you would like to go back: ")
            elif flag:
                if int(edit) > index:
                    print("\nThat's not a valid index :(")
                    edit = input("Please input a valid index or 'return' if you would like to go back: ")
                else:
                    break
            elif edit.lower() == "return":
                continue

        with open(file, 'r') as infile, open("temp.txt", 'w') as outfile:
            for line in infile:
                if edit + "." in line:
                    new_line = input("\nPlease enter your new entry: ")
                    while new_line <= "":
                        print("\nThat's not a valid entry :(")
                        new_line = input("Please input a valid entry or 'return' if you would like to go back: ")
                    if new_line.lower() == "return":
                        continue
                    outfile.write("{} {}: {}\n".format(line[:2], str(today), str(new_line)))
                else:
                    outfile.write(line)
        os.replace('temp.txt', file)
        print("\nSuccessfully edited an entry!")

    # exits the program
    elif command == "exit":
        print("\nHave a great day today! 8)\n")
        exit()
