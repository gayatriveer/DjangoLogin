import bcrypt

#hashing password using Bcrypt

def HashPass(password):
    salt=bcrypt.gensalt()
    hashed=bcrypt.hashpw(password,salt)
    return hashed

