# BMI Calculator 🧮

## Overview
This is a simple Python program that calculates a user's Body Mass Index (BMI) and classifies it into health categories.  
It runs in the terminal and provides clear feedback with input validation.

---

## Features
- Prompt user for **weight (kg)** and **height (m)**
- Calculate BMI using the formula:  

## BMI height and weight
- Classify BMI into categories:
- Underweight (< 18.5)
- Normal (18.5–24.9)
- Overweight (25–29.9)
- Obese (≥ 30)
- Display BMI rounded to 2 decimal places
- Input validation: rejects non-numeric or negative values with helpful error messages

---

## Installation
No external libraries are required. Just ensure you have Python 3 installed.

---

## Usage
Run the program in your terminal:
```bash

Sample Input & Output

Input:
Enter your weight in kg: 70
Enter your height in meters: 1.75
Output:
Your BMI is 22.86 (Normal)


Error Example (negative values):
Enter your weight in kg: -50
Enter your height in meters: 1.75
Error: Weight and height must be positive numbers.


Error Example (non-numeric input):
Enter your weight in kg: abc
Enter your height in meters: 1.75
Error: Please enter numeric values for weight and height.