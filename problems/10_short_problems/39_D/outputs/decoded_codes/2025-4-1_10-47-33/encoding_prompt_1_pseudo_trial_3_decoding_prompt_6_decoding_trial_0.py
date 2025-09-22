# Begin main function

# Step 1: Read two lines of input from the user
first_input = input()  # Read first input line as a string
second_input = input()  # Read second input line as a string

# Step 2: Split the input strings into lists of substrings
first_list = first_input.split()  # Split first input into a list of strings
second_list = second_input.split()  # Split second input into a list of strings

# Step 3: Initialize a counter for differences
difference_count = 0  # Counter for different values

# Step 4: Compare elements from both lists
for index in range(3):  # Loop through index 0 to 2
    # Convert the current elements to integers for comparison
    first_value = int(first_list[index])  # Convert first element to integer
    second_value = int(second_list[index])  # Convert second element to integer

    # Count how many values are different
    if first_value != second_value:  # If values are not equal
        difference_count += 1  # Increment the difference count

# Step 5: Determine the output based on the number of differences
if difference_count < 3:  # If the count of differences is less than 3
    print("YES")  # Print "YES"
else:
    print("NO")  # Print "NO"

# End main function

# This program compares two sets of three values each
# and prints "YES" if there are fewer than three differences, otherwise prints "NO".
