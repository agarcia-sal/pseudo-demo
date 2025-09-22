# Read two lines of input, which represent two strings
first_input = input()
second_input = input()

# Create two lists to hold characters from the input strings, excluding spaces
characters_from_first_input = [char for char in first_input if char != ' ']
characters_from_second_input = [char for char in second_input if char != ' ']

# Initialize a list to store the frequency difference of each character
# ASCII range from A (65) to z (122) includes 58 characters (A-Z: 0-25, a-z: 26-51)
frequency_differences = [0] * 96  # allocate a list of size 96 for the ASCII characters

# Calculate frequency differences for each character
for character_code in range(65, 123):  # ASCII values for A (65) to z (122)
    frequency_in_first_input = characters_from_first_input.count(chr(character_code))
    frequency_in_second_input = characters_from_second_input.count(chr(character_code))
    
    # Store the frequency difference
    frequency_differences[character_code] = frequency_in_first_input - frequency_in_second_input

# Check if all frequency differences are non-negative
all_frequencies_non_negative = True
for frequency in frequency_differences:
    if frequency < 0:
        all_frequencies_non_negative = False
        break  # No need to check further, we found a negative frequency

# Output the result based on frequency check
if all_frequencies_non_negative:
    print("YES")
else:
    print("NO")
