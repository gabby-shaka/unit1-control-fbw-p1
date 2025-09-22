weight = input("Enter your weight in kg: ")
height = input("Enter your height in meters: ")

if weight and height:
    weight = float(weight)
    height = float(height)
    
    bmi = weight / (height ** 2)
    category = "Underweight" if bmi < 18.5 else "Normal weight" if 18.5 <= bmi < 25 else "Overweight" if 25 <= bmi < 30 else "Obesity"
    
    print(f"Your BMI is {bmi:.2f}, which is considered {category}.")