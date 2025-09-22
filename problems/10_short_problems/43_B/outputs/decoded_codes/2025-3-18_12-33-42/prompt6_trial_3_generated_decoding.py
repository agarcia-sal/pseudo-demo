# Read two input strings from the user
first_string = input()
second_string = input()

# Remove spaces from both strings and store the results
cleaned_first_string = first_string.replace(" ", "")
cleaned_second_string = second_string.replace(" ", "")

# Initialize a frequency difference list for character counts
frequency_difference = []

# Calculate the frequency difference for each character from 'A' to 'z'
for ascii_value in range(65, 123):  # ASCII from 'A' (65) to 'z' (122)
    # Convert ASCII value to character
    current_character = chr(ascii_value)
    
    # Count occurrences of the character in both cleaned strings
    count_in_first_string = cleaned_first_string.count(current_character)
    count_in_second_string = cleaned_second_string.count(current_character)
    
    # Calculate the difference in counts and add to frequency difference list
    frequency_difference.append(count_in_first_string - count_in_second_string)

# Check if all differences are non-negative
has_negative_difference = True

for difference in frequency_difference:
    if difference < 0:
        has_negative_difference = False
        break  # Exit loop if any negative difference is found

# Output result based on the presence of negative differences
if has_negative_difference:
    print("YES")
else:
    print("NO")
