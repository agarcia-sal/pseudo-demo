# Start of the program

# Step 1: Read two strings from user input
first_string = input()  # User input for the first string
second_string = input()  # User input for the second string

# Step 2: Remove spaces from both strings
first_string = first_string.replace(" ", "")  # Remove spaces from the first string
second_string = second_string.replace(" ", "")  # Remove spaces from the second string

# Step 3: Initialize a frequency list to store counts of character differences
# There are 256 ASCII characters
character_frequency = [0] * 256  # List initialized to hold counts for each ASCII character

# Step 4: Calculate the frequency of each character
for char in range(32, 127):  # Iterate through printable ASCII characters (from space to ~)
    count_in_first_string = first_string.count(chr(char))  # Count occurrences in the first string
    count_in_second_string = second_string.count(chr(char))  # Count occurrences in the second string
    
    # Calculate the difference in counts and store it in character_frequency
    character_frequency[char] = count_in_first_string - count_in_second_string

# Step 5: Check if all frequency differences are non-negative
is_valid = True  # Initialize the validity flag

for count in character_frequency:
    if count < 0:  # If any count is negative
        is_valid = False  # Set validity to False
        break  # Exit loop since we found an invalid case

# Step 6: Output result based on validity check
if is_valid:
    print("YES")  # All counts are non-negative
else:
    print("NO")  # Found at least one negative count

# End of the program
