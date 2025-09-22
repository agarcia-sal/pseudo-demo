# Gather input strings
first_input_string = input()  # First string from user input
second_input_string = input()  # Second string from user input

# Process strings to remove spaces
first_string = [char for char in first_input_string if char != ' ']  # List of characters from the first string
second_string = [char for char in second_input_string if char != ' ']  # List of characters from the second string

# Initialize frequency differences list
frequency_differences = []  # List to store frequency differences of characters

# Calculate frequency differences for ASCII values from 'A' (65) to 'z' (122)
for char_code in range(65, 123):  # Loop from ASCII 65 to 122
    char = chr(char_code)  # Get the character from ASCII code
    first_count = first_string.count(char)  # Count occurrences in first_string
    second_count = second_string.count(char)  # Count occurrences in second_string

    # Calculate the frequency difference (first minus second)
    frequency_difference = first_count - second_count
    frequency_differences.append(frequency_difference)  # Append to the list

# Determine validity of transformation
if any(diff < 0 for diff in frequency_differences):  # Check for any negative values
    print("NO")  # Not enough characters to match the second string
else:
    print("YES")  # The first string can be transformed to match the second
