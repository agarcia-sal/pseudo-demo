# BEGIN

# Get input from the user, two separate strings
first_input = input()
second_input = input()

# Remove spaces from both input strings
first_string_characters = list(first_input.replace(" ", ""))
second_string_characters = list(second_input.replace(" ", ""))

# Initialize a list to store frequency differences
frequency_differences = []

# For each character in the range from 'A' to 'z'
for character_code in range(ord('A'), ord('z') + 1):
    # Convert character code to character
    current_character = chr(character_code)
    
    # Count occurrences of current_character in first_string_characters
    count_in_first_input = first_string_characters.count(current_character)
    
    # Count occurrences of current_character in second_string_characters
    count_in_second_input = second_string_characters.count(current_character)
    
    # Calculate the difference in counts and add to the list
    difference = count_in_first_input - count_in_second_input
    frequency_differences.append(difference)

# Check if there are any negative differences
negative_count = sum(1 for x in frequency_differences if x < 0)

# Output "YES" if there are no negative differences, otherwise "NO"
if negative_count == 0:
    print("YES")
else:
    print("NO")

# END
