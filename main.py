'''
Welcome to the ALAF program. An awesome program for awesome friends.
'''
import json
from tabulate import tabulate
import textwrap

friends_file = "alaf.json"

def welcome():
    print("Welcome to ALAF!")

def load_friends(friends_file=friends_file):
    try:
        with open(friends_file) as f:
            friends = json.load(f)
    # create an empty list if the file is not there
    except FileNotFoundError:
        friends = []
    except json.JSONDecodeError:
        friends = []
        print(f"Could not load friends from {friends_file}")

    return friends

def save_friends(friends):
    if not friends:
        print("The friends list is empty. Not saving it!")
        return
    with open(friends_file, mode="w") as f:
        # write the friends list to the file object f
        json.dump(friends, f)
    print(f"{len(friends)} written to {friends_file}.")

def instructions():
    print("<INSTRUCTIONS GO HERE> (Remember to make them awesome)")

def menu():
    menu_text=textwrap.dedent('''\

                            ==============================
                            ==== AWESOME FRIENDS LIST ====
                            ====       Main Menu      ====
                            ==============================
                            (L)ist Friends
                            (A)dd Friend
                            (C)lear List
                            (Q)uit

                            Your choice? ''')
    choice = ''
    options = set('lacq')
    while True:
        choice = input(menu_text).strip().lower()
        if choice in options:
            return choice
        print("I didn't understand. Please try again.\n")

def list_friends(friends):
    if not friends:
        print("No friends in list. Add some!")
        return
    # use tabulate later, just print for now
    print(tabulate(friends, headers='keys', tablefmt='fancy_grid'))

def add_friend():
    questions = ["Name", "Phone Number", "Email Address", "Instagram", "Social Security Number"]
    friend = {}

    print("Enter the information for the new friend")
    print("----------------------------------------")

    for question in questions:
        friend[question] = input(f"{question.title()}: ")
    return friend

def exit_list():
    pass

def main():
    '''This function is everything from start to finish'''
    welcome()
    instructions()
    friends = load_friends()
    print(f"{len(friends)} friends loaded from disk.")
    choice = ''
    while choice != 'q':
        choice = menu()
        if choice == 'l':
            list_friends(friends)
        elif choice == 'a':
            new_friend = add_friend()
            friends.append(new_friend)
            print(f'{new_friend["Name"]} added to list')
        elif choice == 'c':
            friends = []
    
    save_friends(friends)
    print("Thank you for using the friends list!")

''' The better way, but optional
if __name__ == "__main__":
    main()
'''

# actually runs the program using the main function
main()
