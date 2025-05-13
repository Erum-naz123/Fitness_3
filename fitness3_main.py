
   #......Name : Fitness1_main.py
#......Module  :  Software foundation 
#......Tutor :  Miss Meenakshi 
#.....Created :  28/04/2025  by  Erum Naz
#.....Description : Python main program file to process fitness data entered by the user.
#............................................................................

# Function to get the user's name
def get_name():
    name = input("Enter your name: ")
    return name

# Function to get the user's age with input validation
def get_age():
    while True:
        try:
            age = int(input("Enter your age: "))
            if age <= 0:
                print("Age must be a positive number. Try again.")
                continue
            return age
        except ValueError:
            print("Invalid input. Please enter a whole number for age.")

# Function to get the user's weight with input validation
def get_weight():
    while True:
        try:
            weight = float(input("Enter your weight in kg: "))
            if weight <= 0:
                print("Weight must be a positive number. Try again.")
                continue
            return weight
        except ValueError:
            print("Invalid input. Please enter a number for weight.")

# Function to get the user's height with input validation
def get_height():
    while True:
        try:
            height_cm = float(input("Enter your height in cm: "))
            if height_cm <= 0:
                print("Height must be a positive number. Try again.")
                continue
            return height_cm
        except ValueError:
            print("Invalid input. Please enter a number for height.")

# Function to convert height from centimeters to meters
def convert_height_cm_to_m(height_cm):
    """Converts height from centimeters to meters."""
    height_m = height_cm / 100
    return height_m

# Function to calculate BMI based on weight and height
def calculate_bmi(weight, height_cm):
    """Calculates BMI using weight (kg) and height (cm)."""
    height_m = convert_height_cm_to_m(height_cm)  # Convert height to meters
    bmi = weight / (height_m ** 2)  # BMI formula
    return bmi

# Function to determine fitness category based on BMI value
def determine_fitness_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi <= 24.9:
        return "Normal weight"
    elif 25 <= bmi <= 29.9:
        return "Overweight"
    else:
        return "Obese"

# Function to calculate maximum heart rate and target heart rate zones
def calculate_heart_rates(age):
    max_heart_rate = 220 - age  # Formula for max heart rate
    moderate_min = int(max_heart_rate * 0.50)  # 50% of max heart rate
    moderate_max = int(max_heart_rate * 0.70)  # 70% of max heart rate
    vigorous_min = int(max_heart_rate * 0.70)  # 70% of max heart rate
    vigorous_max = int(max_heart_rate * 0.85)  # 85% of max heart rate
    return max_heart_rate, (moderate_min, moderate_max), (vigorous_min, vigorous_max)

# Function to display the full fitness report
def display_report(name, age, weight, height_cm, bmi, category, max_heart_rate, moderate_range, vigorous_range):
    print("\n--- Fitness Report ---")
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Weight: {weight} kg")
    print(f"Height: {height_cm} cm")
    print(f"BMI: {bmi:.2f}")  # BMI displayed with 2 decimal points
    print(f"Fitness Category: {category}")
    print(f"Max Heart Rate: {max_heart_rate} bpm")
    print(f"Target Heart Rate (Moderate Intensity): {moderate_range[0]}-{moderate_range[1]} bpm")
    print(f"Target Heart Rate (Vigorous Intensity): {vigorous_range[0]}-{vigorous_range[1]} bpm")
    print("-" * 30)  # Line separator for better display

# Main function that controls the program flow
def main():
    while True:
        # Collect user input
        name = get_name()
        age = get_age()
        weight = get_weight()
        height_cm = get_height()

        # Perform calculations
        bmi = calculate_bmi(weight, height_cm)
        category = determine_fitness_category(bmi)
        max_heart_rate, moderate_range, vigorous_range = calculate_heart_rates(age)

        # Display fitness report
        display_report(name, age, weight, height_cm, bmi, category, max_heart_rate, moderate_range, vigorous_range)

        # Ask user whether to continue or terminate
        option = input("\nEnter 'c' to continue or 't' to terminate: ").lower()
        if option != 'c':
            print("Program terminated.")
            break  # Exit the loop to terminate program

# Program entry point
if __name__ == "__main__":
    main()
