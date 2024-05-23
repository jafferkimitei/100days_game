import hashlib

def hash_password(password):
    # Convert the password string to bytes
    password_bytes = password.encode('utf-8')
    
    # Create a SHA-256 hash object
    hash_object = hashlib.sha256()
    
    # Update the hash object with the password bytes
    hash_object.update(password_bytes)
    
    # Get the hexadecimal representation of the hash
    hashed_password = hash_object.hexdigest()
    
    return hashed_password

def main():
    # Get password input from the user
    password = input("Enter your password: ")
    
    # Hash the password
    hashed_password = hash_password(password)
    
    # Print the hashed password
    print("Hashed Password:", hashed_password)

if __name__ == "__main__":
    main()
