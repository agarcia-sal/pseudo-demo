# Read two strings from the user
first_string = input()
second_string = input()

# Remove all spaces from the input strings
cleaned_first = first_string.replace(" ", "")
cleaned_second = second_string.replace(" ", "")

# Initialize a list to store frequency differences
frequency_differences = []

# Count character frequencies for each character from 'A' to 'z'
for char in range(ord('A'), ord('z') + 1):
    # Convert the ASCII code back to a character
    character = chr(char)
    
    # Count how many times this character appears in cleaned_first
    count_in_first = cleaned_first.count(character)
    # Count how many times this character appears in cleaned_second
    count_in_second = cleaned_second.count(character)
    
    # Calculate the difference and append to the list
    frequency_difference = count_in_first - count_in_second
    frequency_differences.append(frequency_difference)

# Check for negative values in frequency_differences
negative_count = sum(1 for difference in frequency_differences if difference < 0)

# Output the result based on the negative count
if negative_count == 0:
    print("YES")
else:
    print("NO")
