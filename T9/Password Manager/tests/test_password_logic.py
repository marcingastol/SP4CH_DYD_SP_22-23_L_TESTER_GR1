import os
import pytest
from app.password_logic import load_passwords, save_passwords, add_password


def test_load_passwords():
    file_path = os.path.join(os.path.dirname(__file__), "..", "passwords.json")
    passwords = load_passwords(file_path)
    assert "passwords" in passwords
    assert isinstance(passwords["passwords"], list)


def test_save_passwords():
    file_path = os.path.join(os.path.dirname(__file__), "..", "passwords.json")
    test_passwords = {"passwords": []}
    save_passwords(file_path, test_passwords)
    saved_passwords = load_passwords(file_path)
    assert test_passwords == saved_passwords


def test_add_password():
    passwords = {"passwords": []}
    name = "test"
    url = "https://www.test.com"
    username = "test@example.com"
    password = "testp@ss"
    updated_passwords = add_password(passwords, name, url, username, password)
    assert updated_passwords["passwords"][0] == {
        "name": name,
        "url": url,
        "username": username,
        "password": password,
    }


def test_add_multiple_passwords():
    passwords = {"passwords": []}

    entries = [
        {
            "name": "test1",
            "url": "https://www.test1.com",
            "username": "test1@example.com",
            "password": "test1p@ss",
        },
        {
            "name": "test2",
            "url": "https://www.test2.com",
            "username": "test2@example.com",
            "password": "test2p@ss",
        },
        {
            "name": "test3",
            "url": "https://www.test3.com",
            "username": "test3@example.com",
            "password": "test3p@ss",
        },
    ]

    for entry in entries:
        add_password(passwords, **entry)

    assert passwords["passwords"] == entries


def test_add_password_missing_data():
    passwords = {"passwords": []}
    with pytest.raises(TypeError):
        add_password(
            passwords,
            name="test",
            url="https://www.test.com",
            username="test@example.com",
        )


def test_load_passwords_file_not_found():
    file_path = "non_existent_file.json"
    with pytest.raises(FileNotFoundError):
        load_passwords(file_path)
