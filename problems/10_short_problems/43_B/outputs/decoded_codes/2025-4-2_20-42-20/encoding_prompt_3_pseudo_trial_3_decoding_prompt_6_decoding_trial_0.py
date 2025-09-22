# Step 1: Read input
first_string = input()  # Get user input for the first string
second_string = input()  # Get user input for the second string

# Step 2: Remove spaces from both strings
filtered_first_string = [char for char in first_string if char != ' ']  # List of non-space characters from first string
filtered_second_string = [char for char in second_string if char != ' ']  # List of non-space characters from second string

# Step 3: Count character frequency differences
frequency_differences = []  # List to hold frequency differences

# Iterate over ASCII values from 'A' to 'z'
for character_code in range(ord('A'), ord('z') + 1):
    character = chr(character_code)  # Convert ASCII value to character
    count_in_first_string = filtered_first_string.count(character)  # Count occurrences in filtered first string
    count_in_second_string = filtered_second_string.count(character)  # Count occurrences in filtered second string
    difference = count_in_first_string - count_in_second_string  # Calculate the difference
    frequency_differences.append(difference)  # Add the difference to the list

# Step 4: Check if any frequency difference is negative
has_negative_difference = False  # Initialize boolean flag

# Check each difference
for difference in frequency_differences:
    if difference < 0:  # If any difference is negative
        has_negative_difference = True  # Set flag to True
        break  # Exit the loop

# Step 5: Output the result
if not has_negative_difference:  # If there are no negative differences
    print("YES")  # Output yes
else:
    print("NO")  # Output no
