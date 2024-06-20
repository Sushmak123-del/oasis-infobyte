def calculate_bmi(weight, height):
    """
    Calculate BMI using weight in kilograms and height in meters.
    Formula: BMI = weight / (height * height)
    """
    bmi = weight / (height * height)
    return bmi


def classify_bmi(bmi):
    """
    Classify BMI into categories based on WHO guidelines.
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obesity"


def main():
    try:
        # Prompt user for weight in kilograms
        weight = float(input("Enter your weight in kilograms: "))
        # Prompt user for height in meters
        height = float(input("Enter your height in meters: "))

        # Calculate BMI
        bmi = calculate_bmi(weight, height)

        # Classify BMI
        category = classify_bmi(bmi)

        # Display results
        print(f"Your BMI is: {bmi:.2f}")
        print(f"BMI Category: {category}")

    except ValueError:
        print("Error: Please enter valid numeric values for weight and height.")


if __name__ == "__main__":
    main()
