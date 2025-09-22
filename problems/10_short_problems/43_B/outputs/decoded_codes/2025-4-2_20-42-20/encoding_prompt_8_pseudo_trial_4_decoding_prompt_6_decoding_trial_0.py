# Step 1: Initialize Variables
first_input = input().replace(" ", "")  # Store first string input without spaces
second_input = input().replace(" ", "")  # Store second string input without spaces

# Step 2: Count Characters Frequency
character_frequency_difference = []

# Using a loop from ASCII values of 'A' to 'z'
for ascii_value in range(65, 123):  # 65 is 'A', 122 is 'z'
    char = chr(ascii_value)  # Convert ASCII value to character
    count_first = first_input.count(char)  # Count occurrences in first input
    count_second = second_input.count(char)  # Count occurrences in second input
    difference = count_first - count_second  # Calculate the frequency difference
    character_frequency_difference.append(difference)  # Append difference to the list

# Step 3: Evaluate Results
# Count how many values in character_frequency_difference are negative
negative_count = sum(1 for difference in character_frequency_difference if difference < 0)

# Step 4: Output Decision
if negative_count == 0:  # If there are no negative counts
    print("YES")  # Output YES if first_input has enough of each character
else:
    print("NO")  # Output NO otherwise
