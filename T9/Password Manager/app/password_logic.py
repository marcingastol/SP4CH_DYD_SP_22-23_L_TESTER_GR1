import json


def load_passwords(file_path):
    with open(file_path, "r") as file:
        passwords = json.load(file)
    return passwords


def save_passwords(file_path, passwords):
    with open(file_path, "w") as file:
        json.dump(passwords, file)


def add_password(passwords, name, url, username, password):
    passwords["passwords"].append(
        {"name": name, "url": url, "username": username, "password": password}
    )
    return passwords
