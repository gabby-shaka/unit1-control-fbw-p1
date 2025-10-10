#Pyrimad Pattern

# STEP-BY-STEP GUIDE:
# Row O: 4 spaces, 1 star
# Row 1: 3 spaces, 3 stars
# Row 2: 2 spaces 5 stars
# Row 3: 1 space, 7 stars
# Row 4: 0 spaces, 9 stars

rows = 5
#create an outer loop for the rows
#step 1: create an 
for i in range(rows):
    #step 2
    for j in range(rows-i-1):
        print(" ", end="")
        #step 3
        for k in range(2*i+1):
            print("*", end="")
            #4
            print()