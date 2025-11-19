def load_users():
    users = []
    try:
        with open('storage/users.txt', 'r') as file:
            for line in file:
                username, password, user_type = line.strip().split('|')
                users.append({
                    'username': username,
                    'password': password,
                    'type': user_type
                })
    except FileNotFoundError:
        pass
    return users



def save_users(users):
    with open('storage/users.txt', 'w') as file:
        for user in users:
            file.write(f"{user['username']}|{user['password']}|{user['type']}\n")
            
