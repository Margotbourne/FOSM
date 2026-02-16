import bcrypt

def hash_password(password):
    password_bytes = password.encode("utf-8")
    salt = bcrypt.gensalt(12)
    return bcrypt.hashpw(password_bytes, salt)

def compare_password_hash(entered_password, hashed_password):
    password_bytes = entered_password.encode('utf-8')
    return bcrypt.checkpw(password_bytes, hashed_password.encode('utf-8'))


def valid_password(password):
    special_chars = ['!', '@', "£", "$", "%"]
    if len(password) < 7:
        return False
    else:
        has_special = False
        for char in password:
            if char in special_chars:
                has_special = True
        return has_special