import getpass

# Database (username : password)
database = {"taha.cheracher": "123456", "yassine.cheracher": "654321"}

username = input("Enter Your Username: ")

if username in database:
    attempts = 3  # max password attempts
    while attempts > 0:
        password = getpass.getpass("Enter Your Password: ")
        if password == database[username]:
            print("✅ Verified")
            break
        else:
            attempts -= 1
            print("❌ Wrong password! " + str(attempts) + " attempt(s) left.")
    else:
        print("🚫 Access denied. Too many attempts.")
else:
    print("🚫 Username not found.")
