# Helper function to count occurrences of a character in a character list
def count_occurrences(target_char, character_list):
    count = 0  # Initialize count to 0
    for character in character_list:
        if character == target_char:  # Compare each character with the target character
            count += 1  # Increment count if they match
    return count  # Return the final count

# Main part of the program
# Step 1: Accept input
first_string = input()  # Read the first string
second_string = input()  # Read the second string

# Step 2: Remove spaces from both strings
cleaned_string1 = [character for character in first_string if character != ' ']  # List comprehension to remove spaces
cleaned_string2 = [character for character in second_string if character != ' ']  # List comprehension to remove spaces

# Step 3: Calculate frequency differences of characters
frequency_differences = []  # Initialize an empty list to store frequency differences
for ascii_value in range(ord('A'), ord('z') + 1):  # Iterate through ASCII values from 'A' to 'z'
    current_char = chr(ascii_value)  # Convert ASCII value to character
    count_in_first = count_occurrences(current_char, cleaned_string1)  # Count occurrences in first string
    count_in_second = count_occurrences(current_char, cleaned_string2)  # Count occurrences in second string
    frequency_differences.append(count_in_first - count_in_second)  # Append the difference to the list

# Step 4: Check if there are any negative frequency differences
has_negative_frequency = False  # Initialize flag to check negative frequencies
for difference in frequency_differences:  # Iterate through differences
    if difference < 0:  # Check for any negative difference
        has_negative_frequency = True  # Set flag to True if found
        break  # Exit the loop early if a negative is found

# Step 5: Output result
if not has_negative_frequency:  # Check the flag
    print("YES")  # No negative frequencies found
else:
    print("NO")  # Negative frequencies found
