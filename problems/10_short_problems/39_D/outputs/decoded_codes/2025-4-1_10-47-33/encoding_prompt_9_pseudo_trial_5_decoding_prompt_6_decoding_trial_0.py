# Start the program

# Receive two input strings
first_set = input()  # First input string representing a list of three numbers
second_set = input()  # Second input string representing a list of three numbers

# Split both input strings into lists
numbers_first = first_set.split()  # Create a list by dividing first_set into separate numbers
numbers_second = second_set.split()  # Create a list by dividing second_set into separate numbers

# Initialize a counter for differences
difference_count = 0  # Set the difference counter to 0

# Loop through each number in both lists
for index in range(3):  # For each index from 0 to 2
    # Convert the number from numbers_first and numbers_second at the current index from string to an integer
    first_number = int(numbers_first[index])  # Convert to integer
    second_number = int(numbers_second[index])  # Convert to integer
    
    # If the number from numbers_first is not equal to the number from numbers_second
    if first_number != second_number:
        # Increase difference_count by 1
        difference_count += 1

# Evaluate the number of differences
if difference_count < 3:  # If the difference count is less than 3
    print("YES")  # Print "YES"
else:  # Otherwise
    print("NO")  # Print "NO"

# End of the program
