def filtered_list(string):
    # Create a list of characters in the string excluding spaces
    return [char for char in string if char != ' ']

# Step 1: Collect two lines of input
first_input = input()
second_input = input()

# Step 2: Create a list of characters from the first input excluding spaces
filtered_first = filtered_list(first_input)

# Step 3: Create a list of characters from the second input excluding spaces
filtered_second = filtered_list(second_input)

# Step 4: Initialize frequency list
frequency_differences = []

# ASCII code range from 'A' to 'z' includes 65 to 122
for character_code in range(ord('A'), ord('z') + 1):
    character = chr(character_code)
    # Count frequency in each filtered list
    difference = filtered_first.count(character) - filtered_second.count(character)
    frequency_differences.append(difference)

# Step 6: Check if any frequency difference is negative
if any(diff < 0 for diff in frequency_differences):
    print("NO")
else:
    print("YES")
