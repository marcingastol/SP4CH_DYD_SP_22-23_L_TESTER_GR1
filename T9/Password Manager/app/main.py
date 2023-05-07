import os
from app.password_logic import load_passwords, save_passwords, add_password


def main():
    file_path = os.path.join(os.path.dirname(__file__), "..", "passwords.json")
    passwords = load_passwords(file_path)

    new_entry = {
        "name": "test",
        "url": "https://www.test.com",
        "username": "test@example.com",
        "password": "testp@ss",
    }

    updated_passwords = add_password(passwords, **new_entry)
    save_passwords(file_path, updated_passwords)
    print("New entry added successfully!")


if __name__ == "__main__":
    main()
