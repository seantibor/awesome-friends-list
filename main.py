'''
Welcome to the ALAF program. An awesome program for awesome friends.
'''
import json

friends_file = "alaf.json"

def welcome():
    print("Welcome to ALAF!")

def load_friends():
    try:
        with open(friends_file) as f:
            friends = json.load(f)
    # create an empty list if the file is not there
    except FileNotFoundError:
        friends = []

    return friends

def save_friends(friends):
    with open(friends_file, mode="w") as f:
        # write the friends list to the file object f
        json.dump(friends, f)

def instructions():
    print("<INSTRUCTIONS GO HERE> (Remember to make them awesome)")

def menu():
    """ Show the user a menu of things they can do, and return their choice """
    print("Choose an option")
    print("(L)ist Friends")
    print("(A)dd Friend")
    print("(C)lear List")
    print("(Q)uit")
    while True:
        choice = input("Now choose: ").lower().strip()
        if choice in 'lacq':
            return choice
        print("Invalid choice.")

def list_friends(friends):
    # use tabulate later, just print for now
    print(friends)

def add_friend():
    friend = {}
    name = input("What is your friend's name? ")
    friend['Name'] = name
    return friend


def exit_list():
    pass

def main():
    '''This function is everything from start to finish'''
    welcome()
    instructions()
    friends = load_friends()
    action = menu()
    # List Friends
    if action == 'l':
        list_friends(friends)
    # Add Friend
    elif action == 'a':
        new_friend = add_friend()
        friends.append(new_friend)
        print(f"{new_friend['Name']} added.")
    elif action == 'c':
        friends = []
        print("List cleared.")
    
    
    save_friends(friends)

''' The better way, but optional
if __name__ == "__main__":
    main()
'''

# actually runs the program using the main function
main()
