# Username
while True:
    username = input("Enter a username (3-15 chars): ")
    if len(username) < 3:
        print("Too short! Min 3 characters!")
        continue
        
    if len(username) > 15:
        print("Too long! Max 15 characters!")
        continue
    
    for char in username: 
        if char == " ":
            print("No spaces allowed")
            continue
    break 

# Password
while True: 
    password = input("Enter a password: ")
    if len(password) < 8:
        print("Too short!")
        continue
    for char in password: 
        if not('0' <= char <= '9'):
            print("Need one digit")
            continue
        if not('A' <= char <= 'Z'):
            print("Need one letter")
            continue
    break

# Age
while True:
    age = input("Enter your age: ")
    if age.isdigit():
        age = int(age)
        if age < 13:
            print("Too young!")
            continue
        if age > 120:
            print("Too old!")
            continue
    elif age.isdigit() == False:
        print("Enter an integer value")
        continue
    break
    
# Confirmation
    
    