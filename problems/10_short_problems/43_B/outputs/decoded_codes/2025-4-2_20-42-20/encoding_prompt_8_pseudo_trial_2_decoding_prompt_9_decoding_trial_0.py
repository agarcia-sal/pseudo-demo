1. Gather Input Strings:
   - Read the first string from user input.
   - Read the second string from user input.

2. Process Strings to Remove Spaces:
   - Create a list called firstString that contains all characters from the first input string, excluding spaces.
   - Create a list called secondString that contains all characters from the second input string, excluding spaces.

3. Calculate Frequency Differences:
   - Initialize a list called frequencyDifferences to store the difference in character frequencies.
   - For each character code from 'A' (ASCII value 65) to 'z' (ASCII value 122):
     - Count how many times the character appears in firstString.
     - Count how many times the same character appears in secondString.
     - Calculate the difference between the counts (first minus second) and add it to frequencyDifferences.

4. Determine Validity of Transformation:
   - Check if there are any negative values in the frequencyDifferences list.
     - If there are no negative values, this means the first string has all necessary characters in equal or greater amounts compared to the second string.
     - If there are negative values, this means the first string cannot provide enough characters to match those needed in the second string.

5. Output the Result:
   - If the first string can be transformed to match the second string, print "YES".
   - Otherwise, print "NO".


# Gather Input Strings
first_string = input()
second_string = input()

# Process Strings to Remove Spaces
first_characters = [char for char in first_string if char != ' ']
second_characters = [char for char in second_string if char != ' ']

# Calculate Frequency Differences
frequency_differences = []
for char_code in range(ord('A'), ord('z') + 1):
    char = chr(char_code)
    count_first = first_characters.count(char)
    count_second = second_characters.count(char)
    frequency_difference = count_first - count_second
    frequency_differences.append(frequency_difference)

# Determine Validity of Transformation
can_transform = all(diff >= 0 for diff in frequency_differences)

# Output the Result
if can_transform:
    print("YES")
else:
    print("NO")
