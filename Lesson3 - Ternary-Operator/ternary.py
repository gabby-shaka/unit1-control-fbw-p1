# JS TERNARY
'''
let status = age >= 18 ? 'Adult' : 'Minor';
let message = score >= 90 ? "Excellent" : "Keep Trying!"
'''
# Python Ternary 
age = 15 
status = "adult" if age >= 18 else "minor"
score = 75
message = "Excellent" if score >= 90 else "Keep Trying!"

#  Examples
password = "mypass123"
strength = "strong" if len(password) >= 8 else "Weak"
print(f"Password strength: {strength}")

# Combining Ternary + Chaining 
category = ("child" if 0 <= age <= 12 else 
            "teen" if 13 <= age <= 17 else 
            "adult" if 18 <= age <= 64 else 
            "Senior" )


score = 89
grade = ("A" if 90 <= score <= 100 else 
         "B" if 80 <= score <= 89 else 
         "C" if 70<= score <= 79 else 
         "D" if 60 <= score <= 69 else 
         "F")


