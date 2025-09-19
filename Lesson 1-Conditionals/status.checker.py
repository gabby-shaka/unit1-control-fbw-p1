name = input("Enter your name: ")
age = int(input("Enter your age: "))
print (name)

age = int(input("Enter your age (16-100): "))

if 16 <= age <= 100:
    print (age)
else:
    print ("Age must be between 16 and 100")
    
gpa = float(input("Enter your GPA (0.0 - 4.0): "))
if 0.0 <= gpa <= 4.0:
    print (gpa)
else:
 print("GPA must be between 0.0 and 4.0.")
    
 check_eligibility(age, gpa):
    enrollment = age >= 18 and gpa >= 2.0
    voting = age >= 18
    honor_roll = gpa >= 3.5
    print (enrollment, voting, honor_roll)
    
    name = (name)
age = (age)
gpa = (gpa)
enrollment, voting, honor_roll = check_eligibility(age, gpa)


print("\n--- Results ---")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"GPA: {gpa:.2f}")

print(f"Enrollment Eligibility: {'Yes' if enrollment else 'no'}")
print(f"Voting Eligibility: {'Yes' if voting else 'no'}")
print(f"Honor Roll: {'yes' if honor_roll else 'no'}")