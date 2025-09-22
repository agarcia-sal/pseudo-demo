# Start the program.

# Receive Input
first_set = input()  # Read the first set of numbers
second_set = input()  # Read the second set of numbers

# Process Input
first_numbers = first_set.split()  # Split the first set into individual numbers
second_numbers = second_set.split()  # Split the second set into individual numbers

# Initialize Differences Counter
difference_count = 0  # Initialize the counter for differences

# Compare Numbers
for index in range(3):  # For each index from 0 to 2
    first_number = int(first_numbers[index])  # Get the number from the first set
    second_number = int(second_numbers[index])  # Get the number from the second set
    if first_number != second_number:  # Check if the numbers are different
        difference_count += 1  # Increment the difference counter

# Determine Output
if difference_count < 3:  # If the count of differences is less than 3
    print("YES")  # Print YES
else:  # Otherwise
    print("NO")  # Print NO

# End the program.
