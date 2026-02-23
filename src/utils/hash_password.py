from bcrypt import checkpw, hashpw, gensalt


def generate_password_hash(password: str):
    salt = gensalt()
    hashed_password = hashpw(password=password.encode(), salt=salt)
    return hashed_password.decode()


def check_password_hash(password: str, hashed_password: str):
    return checkpw(hashed_password=hashed_password.encode(), password=password.encode())
