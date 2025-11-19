from storage.data import load_users, save_users


users = load_users()


def register_user():
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("                             USER REGISTRATION FOR AIRLINE RESERVATION SYSTEM                        ")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
    
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    
    print("Register as: ")
    print("1. Admin")
    print("2. Simple user")
    
    
    choice = input("Enter your choice (1 or 2): ")
    
    if choice == '1':
        user_type = 'admin'
    elif choice == '2':
        user_type = 'simpleUser'
    else:
        print("Invalid choice. Registration failed.")
        return
    
    
    for user in users:
        if user['username'] == username:
            print("Username already exists. Registration failed.")
            return
        
    new_user = {
        'username': username,
        'password': password,
        'type': user_type
    }
    
    users.append(new_user)
    save_users(users)
    
    print(f"Registration successful! You have registered as a {user_type}.\n You can now log in.")
    




