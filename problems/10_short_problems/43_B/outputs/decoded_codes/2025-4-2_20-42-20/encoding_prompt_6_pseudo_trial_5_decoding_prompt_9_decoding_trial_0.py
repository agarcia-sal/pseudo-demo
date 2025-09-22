# Function to remove spaces from a string
def remove_spaces(string):
    return string.replace(" ", "")

# Read two strings from user input
first_string = input()
second_string = input()

# Remove spaces from both strings
first_string = remove_spaces(first_string)
second_string = remove_spaces(second_string)

# Create a list to store counts of character differences (ASCII size 256)
character_frequency = [0] * 256

# Calculate the frequency of each character
for character in range(256):  # ASCII range from 0 to 255
    count_in_first_string = first_string.count(chr(character))
    count_in_second_string = second_string.count(chr(character))
    
    # Calculate the difference in counts and store it in character_frequency
    character_frequency[character] = count_in_first_string - count_in_second_string

# Check if all frequency differences are non-negative
is_valid = True

for count in character_frequency:
    if count < 0:
        is_valid = False
        break  # Exit loop early if a negative count is found

# Output result based on validity check
if is_valid:
    print("YES")
else:
    print("NO")
