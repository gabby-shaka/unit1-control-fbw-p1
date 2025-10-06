# syntax:
'''
initialize variable
while condition(test variable):
    code block
'''
# count to 5 
num = 5 
while num > 0:
    print(num)
    num -= 1
    print("BLASTOFF!!")
    

# sum of num 1-10
num = 1
total = 0


while num <= 10:
    total += num #(total = total +num)
    num += 1
    
print(f"Sum of numbers 1-10: {total}")



while num <= 10:
    total += num
    if num < 10:
       print(num, end="+") 
    else: 
        print (num, end="=")
        num += 1
    print(total)
    print()
    
    # sum of digitd
    # take a user input as int, and sum the digits of it
    number = input("Enter a number:")
    sum = 0
#     for char in number:
#         print(f"{char} {type(char)}") 
#         sum += int(char)
# print(f"Total {sum}")

i=0
while i<len(number):
    sum += int(number[i])
    i += 1
print(f"Total {sum}")

# Algorithm - sum of  digits (as ints)
number = int(input("Enter a Number!"))
sum = 0 
while number > 0:
    # Get the last digit
    digit = number % 10 
    sum += digit  #add to sum
    number = number // 10 #remove the last digit
    
print(f"The sum of the digitd {number}: {sum}")



# Algorithm - count digits (as ints)
number = 54321
count = 0 

while number > 0:
    count += 1
number = number // 10 # Remove the last digit
print(f"The number {number} has {count} digits!")

