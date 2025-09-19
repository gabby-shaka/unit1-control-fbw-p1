# ========================================
# ACCELERATED PYTHON UNIT 2 - LESSON 1
# Conditionals: JavaScript to Python
# ========================================

# ========================================
# SECTION 1: QUICK TRANSLATION CHALLENGE
# ========================================
print("==GRADE CLASSIFICATION==")
score = 87
if score >= 90:
    print("A grade!")
elif score >= 80:
    print("B grade!")
else:
    print("Below B")

# ========================================
# SECTION 2: AGE CATEGORY CLASSIFIER
# ========================================
age = input("Enter your age: ")
if (0 <= age <= 12):
    print("You are a child")
elif (13 <= age <= 19):
    print("You are a teenager")
elif (20 <= age <= 64):
    print("You are an adult")
elif (age >= 65):
    print("You are a senior")
else:
    print("Please enter a valid age!")


# ========================================
# SECTION 3: STUDENT STATUS CHECKER
# ========================================
age = 17
gpa = 3.8 
has_liscense = True

can_drive = age >= 16 and has_liscense
honor_roll = gpa >= 3.5
eligible = can_drive and honor_roll and age >= 17 

print(f"Can Drive: {can_drive}")
print(f"Honor Roll: {honor_roll}")
print(f"Eligible: {eligible}")

if eligible:
    

# ========================================
# SECTION 4: GRADE VALIDATOR CHALLENGE
# ========================================


# ========================================
# SECTION 5: WEATHER DECISION SYSTEM
# ========================================
    print