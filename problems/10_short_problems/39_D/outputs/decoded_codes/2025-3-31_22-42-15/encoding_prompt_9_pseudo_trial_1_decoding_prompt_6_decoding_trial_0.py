# Start Program

# Receive Input: Read the first and second sets of numbers
first_set = input()
second_set = input()

# Split Input into Individual Numbers
first_numbers = first_set.split()
second_numbers = second_set.split()

# Initialize Difference Count
difference_count = 0

# Compare the Numbers
for position in range(3):  # There are 3 numbers to compare
    first_number = int(first_numbers[position])  # Convert first number to integer
    second_number = int(second_numbers[position])  # Convert second number to integer
    
    # Check if the numbers are different
    if first_number != second_number:
        difference_count += 1  # Increment difference count if they are not equal

# Evaluate Differences
if difference_count < 3:
    print("YES")  # Print "YES" if differences are less than 3
else:
    print("NO")   # Print "NO" if differences are 3 or more

# End Program
