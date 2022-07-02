import bcrypt


def HashPass(password):
    salt=bcrypt.gensalt()
    hashed=bcrypt.hashpw(password,salt)
    return hashed