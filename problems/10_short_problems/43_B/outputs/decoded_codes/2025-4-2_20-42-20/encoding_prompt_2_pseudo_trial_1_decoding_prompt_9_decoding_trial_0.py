# Read the first string from input
first_string = input()
# Read the second string from input
second_string = input()

# Remove all spaces from both strings
cleaned_first_string = first_string.replace(" ", "")
cleaned_second_string = second_string.replace(" ", "")

# Initialize a list to hold the frequency differences of characters
character_frequencies = []

# Iterate over the ASCII range from 'A' to 'z'
# Note: This range includes letters from A-Z and a-z, which are represented by their ASCII codes
for char in range(ord('A'), ord('z') + 1):
    # Count occurrences in both cleaned strings
    count_first = cleaned_first_string.count(chr(char))
    count_second = cleaned_second_string.count(chr(char))
    
    # Calculate the difference in frequencies and append to the list
    frequency_difference = count_first - count_second
    character_frequencies.append(frequency_difference)

# Count how many elements in character_frequencies are negative
negative_count = sum(1 for freq in character_frequencies if freq < 0)

# Evaluate the results based on the negative count
if negative_count == 0:
    print("YES")  # There are enough characters in the first string
else:
    print("NO")   # Not enough characters in the first string
