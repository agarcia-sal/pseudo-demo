# Function to determine if one string can be transformed into another
def can_transform_string():
    # Gather input strings
    first_input = input()  # Read the first string from user input
    second_input = input()  # Read the second string from user input

    # Process strings to remove spaces
    first_string = [char for char in first_input if char != ' ']  # List of characters from the first string excluding spaces
    second_string = [char for char in second_input if char != ' ']  # List of characters from the second string excluding spaces

    # Initialize frequency difference list
    frequency_differences = [0] * 58  # List to hold frequency differences for characters A-z (ASCII 65 to 122)

    # Calculate frequency differences for characters
    for char_code in range(65, 123):  # ASCII range for A-Z and a-z
        first_count = first_string.count(chr(char_code))  # Count occurrences in first string
        second_count = second_string.count(chr(char_code))  # Count occurrences in second string
        frequency_differences[char_code - 65] = first_count - second_count  # Store frequency difference

    # Determine validity of transformation
    if any(diff < 0 for diff in frequency_differences):  # Check for negative values in frequency differences
        print("NO")  # Not enough characters to transform
    else:
        print("YES")  # Transformation possible

# Call the function to execute
can_transform_string()
