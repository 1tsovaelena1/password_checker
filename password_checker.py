import sqlite3
from datetime import datetime

conn=sqlite3.connect("saved_inf.db")
cursor=conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS saved_inf (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               user_firstname TEXT,
               user_lastname TEXT,
               checked_at TEXT,
               password_length INTEGER,
               has_uppercase INTEGER,
               has_lowercase INTEGER,
               has_digit INTEGER,
               has_special INTEGER
)               
""")
conn.commit()

firstname=input("Enter your first name:")
lastname=input("Enter your last name:")
messages = [
    "Enter your password. Your password should be strong and contains:",
    "At least 12 characters.",
    "At least one uppercase character.",
    "At least lowercase characters.",
    "At least one special character.",
    "At least 1 number."
]

for msg in messages:
    print(msg)

max_attempts=3
attempt=0

def check_password(password):
    has_uppercase=False # alway use flag=False/ bc if we need to find something in string
    has_lowercase=False
    has_digit=False
    has_characters=False
    has_norepeats=True
    seen_chars=set()

    for c in password:
        if c.isupper():
            has_uppercase=True #if we find uppercase - that's gonna be True
        elif c.islower():
            has_lowercase=True
        elif c.isdigit():
            has_digit=True
        elif not c.isalnum():
            has_characters=True

        if c in seen_chars:
            has_norepeats=False
        else:
            seen_chars.add(c)

    return {
        "uppercase": has_uppercase, #create a key where is True or False
        "lowercase": has_lowercase,
        "digit": has_digit,
        "special": has_characters,
        "norepeats": has_norepeats
    }

while attempt<max_attempts:
    password=input("Enter your password: ")

    flags=check_password(password)

    if len(password)>=12:
         print("✅Done - your password contains 12 characters!")
    else:
        print("Error. Your password needs at least 12 characters!")
    if flags["uppercase"]:
        print("✅Done - your password contains at least one uppercase character!")
    else:
        print("Error. Your password needs at least one uppercase character!")
    if flags["lowercase"]:
        print("✅Done - your password contains at least one lowercase character!")
    else:
        print("Error. Your password needs at least one lowercase character!")
    if flags["digit"]:
        print("✅Done - your password contains at least one number!")
    else:
        print("Error. Your password needs at least one number!")
    if flags["special"]:
        print("✅Done - your password contains at least one number!")
    else:
        print("Error. Your password needs at least one character!")
    if flags["norepeats"]:
        print("✅Done - No repeating characters!")
    else:
        print("❌ Password contains repeating characters!")



    if len(password) >= 12 and flags["uppercase"] and flags["lowercase"] and flags["digit"] and flags["special"] and flags["norepeats"]:
        print("Well done! Your password is strong!")
        break
    else:
        attempt += 1
        print("❌ Password is not strong enough.")
        if attempt < max_attempts:
            print(f"Try again! Attempts left: {max_attempts - attempt}")
        else:
            print("❌ Maximum attempts reached. Please restart the program.")

cursor.execute("""
INSERT INTO saved_inf (
               user_firstname, user_lastname,
               checked_at, password_length,
               has_uppercase, has_lowercase,
               has_digit, has_special)
               VALUES(?, ?, ?, ?, ?, ?, ?, ?)
""", (
    firstname,
    lastname,
    datetime.now().isoformat(),
    len(password),
    int(flags["uppercase"]),
    int(flags["lowercase"]),
    int(flags["digit"]),
    int(flags["special"])
))
conn.commit()

cursor.execute ("""
SELECT user_firstname, user_lastname, 
        checked_at, password_length
FROM saved_inf
""")
rows=cursor.fetchall()
for row in rows:
    print(row)

conn.close()

