# Read two strings from user input
first_input = input()
second_input = input()

# Remove spaces from both inputs
cleaned_first_input = first_input.replace(" ", "")
cleaned_second_input = second_input.replace(" ", "")

# Initialize a frequency difference list to track character count differences
frequency_differences = []

# For each character in the range from 'A' to 'z'
for character_code in range(ord('A'), ord('z') + 1):
    # Count occurrences in each cleaned input
    count_in_first_input = cleaned_first_input.count(chr(character_code))
    count_in_second_input = cleaned_second_input.count(chr(character_code))
    
    # Calculate the difference in counts and add to the frequency_differences list
    frequency_differences.append(count_in_first_input - count_in_second_input)

# Check if all frequency differences are non-negative
non_negative_count = sum(1 for difference in frequency_differences if difference < 0)

# Output the result based on whether any negative counts were found
if non_negative_count == 0:
    print("YES")
else:
    print("NO")
