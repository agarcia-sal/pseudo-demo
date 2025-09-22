# Start of the program

# Read two input strings from the user
first_input = input()  # First input string
second_input = input()  # Second input string

# Remove spaces from both input strings
first_processed_string = [char for char in first_input if char != ' ']  # List of characters excluding spaces
second_processed_string = [char for char in second_input if char != ' ']  # List of characters excluding spaces

# Initialize a frequency list to hold character count differences
# There are 58 ASCII characters from 'A' (65) to 'z' (122), thus creating a list of 58 zeros
character_frequency_differences = [0] * (123 - 65)  # 58 elements initialized to zero

# Calculate the differences in character frequencies between the two strings
for ascii_value in range(65, 123):  # From 'A' to 'z'
    current_character = chr(ascii_value)  # Get the character corresponding to the ASCII value
    count_in_first_string = first_processed_string.count(current_character)  # Count occurrences in first string
    count_in_second_string = second_processed_string.count(current_character)  # Count occurrences in second string
    frequency_difference = count_in_first_string - count_in_second_string  # Calculate frequency difference
    character_frequency_differences[ascii_value - 65] = frequency_difference  # Store the difference

# Check if there are any negative differences in the frequency
negative_count = len([num for num in character_frequency_differences if num < 0])  # Count negative differences

# Determine the final output based on negative counts
if negative_count == 0:
    print("YES")  # There are no negative frequency differences
else:
    print("NO")  # There are negative frequency differences

# End of the program
