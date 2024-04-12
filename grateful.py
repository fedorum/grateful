import os
import datetime
import random

today = datetime.date.today().strftime("%d %B %Y")
gfile = 'grateful.txt'

print("Welcome to the grateful.py module!")

while True:
    entry = input('\n' + "What would you like to do? (entry/ view/ delete/ exit) ")
    if entry == "entry":
        grateful = input("What do you feel grateful about today? ")
        if grateful > "":
            with open(gfile, 'a') as g:
                g.write('\n' + str(today) + ": " + str(grateful))
            print('\n' + "New entry created!")
    elif entry == "view":
        print('\n' + "Here's something you were grateful for on" + '\n')
        with open(gfile, 'r') as g:
            lines = g.readlines()
            print(random.choice(lines))
        viewall = input("Would you like to view everything you've been grateful for? ")
        if viewall == "Yes":
            print('\n' + "Here's everything you've been grateful for!")
            with open(gfile, 'r') as g:
                print(g.read())
        elif viewall == "No":
            continue
    elif entry == "delete":
        delete = input("Which entry would you like to delete? (DD Mmm YYYY) ")
        if delete > "          ":
            with open(gfile, 'r') as infile, open("temp.txt", 'w') as outfile:
                for line in infile:
                    if delete not in line.strip('\n'):
                        outfile.write(line)
            os.replace('temp.txt', gfile)
            print("You've deleted a record from " + delete + "!")
        else:
            print("No records were deleted.")
            continue
        # with open('grateful.txt', 'r+') as g:
        #     for line in g:
    # elif entry == "edit":
    #     edit = input("Which entry would you like to edit? (date of entry - DD MMMM YYYY) ")
        # with open('grateful.txt', 'r+') as g:
            # for line in g:
            #     if line.contains(str(edit)):
            #         print(line)
    elif entry == "exit":
        print("Have a great day today! 8)")
        exit()

# notes
# add a function to overwrite existing entries
