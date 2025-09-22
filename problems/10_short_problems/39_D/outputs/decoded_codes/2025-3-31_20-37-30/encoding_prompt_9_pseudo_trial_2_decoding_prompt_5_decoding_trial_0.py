# Start Program

# Receive Input:
first_set = input()  # Get the first set of numbers as a string
second_set = input()  # Get the second set of numbers as a string

# Split Input Strings into Lists:
numbers_set1 = first_set.split()  # Convert the first set string into a list of strings
numbers_set2 = second_set.split()  # Convert the second set string into a list of strings

# Initialize a Counter:
difference_count = 0  # Track the number of differing positions

# Compare Each Position:
for index in range(3):  # Loop through the indices 0 to 2
    num1 = int(numbers_set1[index])  # Convert the first number to an integer
    num2 = int(numbers_set2[index])  # Convert the second number to an integer
    if num1 != num2:  # Check for differences
        difference_count += 1  # Increase the difference count if they are not equal

# Output the Result:
if difference_count < 3:
    print("YES")  # Output YES if differences are less than 3
else:
    print("NO")   # Output NO if differences are 3 or more

# End Program
