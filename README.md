# Password Checker

**Password Checker** is a practical Python tool created by a cybersecurity student to help users generate and validate **strong passwords**, addressing one of today’s most common security risks.  

With this program, users get **real-time guidance** to improve password strength and protect their digital accounts.

## Key Features

- Interactive input for first name, last name, and password  
- Checks for:
  - Minimum 12 characters  
  - Uppercase & lowercase letters  
  - Numbers (at least 1)  
  - Special characters  
  - No repeating characters  
- Modular **Python functions** for readability and maintainability  
- Logs password info (length, character types) in a local SQLite database (`saved_inf.db`)  
- Displays previously checked entries to track password validation history  
- Demonstrates practical use of **programming fundamentals**, **data handling**, and **cybersecurity practices**  

## Why It Matters

This project shows my ability to:

- Solve real-world problems with practical solutions  
- Apply cybersecurity awareness in software development  
- Build user-focused, everyday tools using Python  

## Tech Stack

- Python 3.8+  
- `sqlite3` library  

## How to Run

```bash
git clone https://github.com/1tsovaelena1/password_checker.git
cd password_checker
python password_checker.py
