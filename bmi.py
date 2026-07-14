 #BMI calculator program

def calculate_bmi(weight, height):
    """Calculate BMI and return value + category."""
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi <= 24.9:
        category = "Normal"
    elif 25 <= bmi <= 29.9:
        category = "Overweight"
    else:
        category = "Obese"
    return round(bmi, 2), category

def main():
    try:
        # Ask user height and weight
        weight = float(input("Enter your weight in kg: "))
        height = float(input("Enter your height in meters: "))
        
        if weight <= 0 or height <= 0:
            print("Error: Weight and height must be positive numbers.")
            return
        
        bmi, category = calculate_bmi(weight, height)
        #display result
        print(f"Your BMI is {bmi} ({category})")
    except ValueError:
        print("Error: Please enter numeric values for weight and height.")

if __name__ == "__main__":
    main()
