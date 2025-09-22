# Input Phase
first_line = input().strip()  # Read the first line of input and remove leading/trailing spaces
second_line = input().strip()  # Read the second line of input and remove leading/trailing spaces

# Remove spaces from both lines
string1 = first_line.replace(" ", "")
string2 = second_line.replace(" ", "")

# Frequency Calculation Phase
frequency_differences = []  # Initialize an empty list to store frequency differences

# Loop through the range of character codes from 'A' (65) to 'z' (122)
for char_code in range(ord('A'), ord('z') + 1):
    char = chr(char_code)  # Convert character code to character
    
    # Count occurrences of char in string1 and string2
    count_in_string1 = string1.count(char)
    count_in_string2 = string2.count(char)
    
    # Calculate the difference and append to the frequency differences list
    difference = count_in_string1 - count_in_string2
    frequency_differences.append(difference)

# Result Evaluation Phase
# Check if there are no negative values in the frequency differences list
if all(diff >= 0 for diff in frequency_differences):  # Checking for non-negative values
    print("YES")  # Output "YES" if condition is satisfied
else:
    print("NO")   # Output "NO" if at least one negative value exists
