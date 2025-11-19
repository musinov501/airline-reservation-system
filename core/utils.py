from storage.data import load_users

def view_users():
    users = load_users()
    if not users:
        print("No users found.")
        return
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("                                         LIST OF USERS                                               ")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    
    for i in range(len(users)):
        user = users[i]
        print(f"{i + 1}. Username: {user['username']}, Type: {user['type']}")
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("Press Enter to return to admin panel...")
    
    
