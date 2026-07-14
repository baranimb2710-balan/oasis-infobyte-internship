# Random Password Generator 🔑

## Overview
This is a Python-based command-line tool that generates random passwords based on user preferences.  
It allows you to choose the length and which character types to include (uppercase, lowercase, digits, symbols).

---

## Features
- Prompt user for desired password length (minimum 8 characters)
- Options to include:
  - Uppercase letters (A–Z)
  - Lowercase letters (a–z)
  - Digits (0–9)
  - Symbols (punctuation characters)
- Input validation:
  - Rejects lengths less than 8
  - Rejects if no character types are selected
- Generates a random password using Python’s `random` and `string` libraries
- Allows repeated generation until the user chooses to exit

---

## Tech Stack
- Python 3
- Standard libraries: `random`, `string`

---

## Installation
No external libraries are required. Just ensure you have **Python 3** installed.

---

## Usage
Run the program in your terminal:
```bash
python password_generator.py


Sample Input & Output
✅ Normal Case
Input:
Enter password length (min 8): 12
Include uppercase? (y/n): y
Include lowercase? (y/n): y
Include digits? (y/n): y
Include symbols? (y/n): n
Output:
Generated password: aK9dLx2mQwZp
Generate another? (y/n): n


⚠️ Error Case (Length Too Short)
Input:
Enter password length (min 8): 5
Include uppercase? (y/n): y
Include lowercase? (y/n): y
Include digits? (y/n): y
Include symbols? (y/n): y
Output:
Invalid input. Try again.


⚠️ Error Case (No Character Types Selected)
Input:
Enter password length (min 8): 10
Include uppercase? (y/n): n
Include lowercase? (y/n): n
Include digits? (y/n): n
Include symbols? (y/n): n
Output:
Invalid input. Try again.