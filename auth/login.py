from storage.data import load_users
from panels.admin_panel import admin_dashboard
from panels.user_panel import simple_user_dashboard

def login_user():
    users = load_users()
    
    username = input("Enter your username: ").strip()
    password = input("Enter your password: ").strip()
    

    for user in users:
        if user['username'] == username and user['password'] == password:
            print(f"Login successful! Welcome back, {username}. You are logged in as a {user['type']}.")
            
            if user['type'] == 'admin':
                print("Redirecting to admin dashboard...")
                return admin_dashboard()
            elif user['type'] == 'simpleUser':
                print("Redirecting to user dashboard...")
                return simple_user_dashboard()
    

    print("Invalid username or password. Login failed.")
    return
