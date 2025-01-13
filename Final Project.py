#Kabir Sinha
#CMP 131
#Final Project: Password Manager
#This program was coded for the creation and management
#of passwords and their associated websites

#menu options defined as gloabl constants
VIEW_PW = 1
LOOKUP_PW = 2
ADD_PW = 3
UPDATE_PW = 4
DELETE_PW = 5
EXIT_PW_MGR = 6

import random

def main(): #main program function

    passwords = {} #empty passwords dictionary

    select = 0 #user option variable initiation

    while select != EXIT_PW_MGR:

        select = choose_option()    #get user choice if option isn't to quit program

        if select == VIEW_PW:       #option to view websites/passwords
            view(passwords)

        elif select == LOOKUP_PW:   #option to look up a password using a website
            search_for(passwords)

        elif select == ADD_PW:      #option to add a password to a website
            add(passwords)

        elif select == UPDATE_PW:   #option to change a password
            change(passwords)

        elif select == DELETE_PW:   #option to a delete a password
            delete(passwords)


def choose_option():                        #choose_option function displays menu for user
    print("--Kabir's Password Manager--")   #and gets input from them
    print()
    print('(1) View Existing Passwords')
    print('(2) Search for a Password')
    print('(3) Make a New Password')
    print('(4) Change a Password')
    print('(5) Delete a Password')
    print('(6) Leave the Manager')
    print()

    select = int(input("What's your choice?  ")) #get user's selection

    while select < VIEW_PW or select > EXIT_PW_MGR:
        select = int(input("Enter a valid option: "))

    return select #return's user's selection

def view(passwords):    #define the function to see the websites/passwords dictionary
    for website in passwords:
        key = website #assigns each website as a key in each key-value pairing
        value = passwords[website] #assigns each password as a value in each key-value pairing
        print(f'{key}: {value}\n') #prints the dictionary
        print()


def write_passwords_to_file(passwords):
    outfile = open('sites_and_passwords.txt', 'w')
    for website in passwords:
        key = website
        value = passwords[website]
        outfile.write(f'{key}:{value}\n')

    outfile.close()
    print()



def search_for(passwords):  #defins the function for searching a password using a website
    
    search = input('Enter a website: ') #search for a website to look up a password (website name only: i.e. google)
    if search in passwords:
        print(passwords.get(search)) #prints password for the searched website
    else:
        print('Website not found :/') #prints if the website isn't found
        print()


def generateStrongPW(pwlength=10):      #function for generating random passwords
        #Make a list of all possibilities
        possibilities = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789$#@(*"
        #Start with an empty string
        strongPW = ""
        #Get the desired number of characters and build the strong pw
        for counter in range(pwlength):
            strongPW += random.choice(possibilities)

        return strongPW


def add(passwords): #defines the function for adding a password to a website

    search = input('Enter a website: ') #search a website to ensure it's not in dictionary
    strongPW = generateStrongPW()
    
    if search not in passwords:
        passwords[search] = strongPW  #adds new website to dictionary
        return strongPW #creates a password for the website
        
    else:
        print('This website and password exist') #prints if the website/password exist
        print()


def change(passwords):  #defines the function for changing a password
    
    search = input('Enter a website: ') #look for a website to alter a password
    if search in passwords:
        pw = input('Enter a new password: ') #prompt for a new password

        passwords[search] = pw #adds new password to dictionary
    else:
        print('unknown password or website :/') #prints is website is not found
        print()


def delete(passwords):
    search = input('Enter a website: ') #look for a website to find a password

    if search in passwords:
        if input('Delete this website & password?[Y/N]  ') == 'Y' or 'y':
            del passwords[search]   #deletes a website/password that is searched after confirmation
        else:
            print('Website/password untouched') #prints if password is not deleted
    else:
        print('Website/password unknown') #prints if website isn't found
        print()

if __name__ == '__main__':
    main()
