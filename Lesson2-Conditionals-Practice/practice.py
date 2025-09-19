age = input("Enter your age: ")
G = "G"
PG = "PG"
PG_13 = "PG-13"
R = "R"
if age:
    age = int(age)
    
    rating = input("Enter the movie rating (G, PG, PG-13, R): ")
    
    if rating == G:
        print("You can watch the movie.")
    elif rating == PG: 
        if age >= 10:
            print("You can watch the movie.")
    elif rating == PG_13:
        if age >= 13:
            print("You can watch the movie.")
        else:
            print("You cannot watch the movie.")
    elif rating == R:
        if age >= 17:
            print("You can watch the movie.")
        else:
            print("You cannot watch the movie.")
    else:
        print("Invalid movie rating.")
else:
    print("Invalid age input.")
    
    

    
