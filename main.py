
from auth.register import register_user
from auth.login import login_user
from storage.data import load_users


def main_menu():
    while True:
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("                             WELCOME TO AIRLINE RESERVATION SYSTEM                                         ")
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
        print("1. Register ")
        print("2. Login ")
        print("3. Exit ")
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")        
        choice = input("Enter your choice: ")
        if choice == '1':
            register_user()
            break
        elif choice == '2':
            login_user()
            break
        elif choice == '3':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
            
main_menu()