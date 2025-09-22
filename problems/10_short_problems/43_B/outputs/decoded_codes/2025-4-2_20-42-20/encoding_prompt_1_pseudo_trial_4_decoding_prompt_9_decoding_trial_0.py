# Read the first string from user input and remove any spaces
first_string = input().replace(" ", "")

# Read the second string from user input and remove any spaces
second_string = input().replace(" ", "")

# Initialize a list to hold the frequency differences of all characters from 'A' to 'z'
frequency_difference = [0] * (123 - 65)  # ASCII values from 'A' (65) to 'z' (122)

# Calculate the frequency of characters in both strings
for ascii_value in range(65, 123):  # Iterate from 'A' to 'z'
    char = chr(ascii_value)
    count_in_first = first_string.count(char)  # Count occurrences in the first string
    count_in_second = second_string.count(char)  # Count occurrences in the second string
    
    # Calculate the difference and store it in the list
    frequency_difference[ascii_value - 65] = count_in_first - count_in_second  # Store the difference

# Count how many differences are negative
negative_count = sum(1 for diff in frequency_difference if diff < 0)

# Check if there are any negative differences
if negative_count == 0:
    print("YES")  # All characters in first_string meet the condition
else:
    print("NO")   # At least one character in first_string does not meet the condition
