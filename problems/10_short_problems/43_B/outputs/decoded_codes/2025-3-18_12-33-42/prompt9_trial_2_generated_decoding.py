# Receive input from the user
first_string = input()
second_string = input()

# Prepare strings by removing spaces and creating character lists
characters_in_first = [char for char in first_string if char != ' ']
characters_in_second = [char for char in second_string if char != ' ']

# Initialize a list to hold the frequency differences
character_frequency_difference = []

# Count character frequencies for each character in the ASCII range
for char_code in range(65, 123):  # From 'A' (65) to 'z' (122)
    char = chr(char_code)  # Get the corresponding character from the ASCII value
    count_in_first = characters_in_first.count(char)  # Count occurrences in the first string
    count_in_second = characters_in_second.count(char)  # Count occurrences in the second string
    
    # Compute the frequency difference
    difference = count_in_first - count_in_second
    character_frequency_difference.append(difference)

# Determine the output based on the frequency differences
if any(diff < 0 for diff in character_frequency_difference):  # Check for any negative differences
    print("NO")
else:
    print("YES")
