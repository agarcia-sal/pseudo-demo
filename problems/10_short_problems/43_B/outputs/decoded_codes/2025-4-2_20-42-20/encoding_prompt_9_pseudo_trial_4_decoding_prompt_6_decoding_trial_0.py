# Step 1: Receive Input
first_string = input()  # Get the first string from user input
second_string = input()  # Get the second string from user input

# Step 2: Process Input
cleaned_first_string = first_string.replace(" ", "")  # Remove spaces from the first string
cleaned_second_string = second_string.replace(" ", "")  # Remove spaces from the second string

# Step 3: Initialize Frequency Count
character_frequencies = []  # List to hold the frequency differences

# Step 4: Count Character Frequencies
for character in range(ord('A'), ord('z') + 1):  # Iterate through character range from 'A' to 'z'
    count_in_first = cleaned_first_string.count(chr(character))  # Count character in first string
    count_in_second = cleaned_second_string.count(chr(character))  # Count character in second string
    difference = count_in_first - count_in_second  # Calculate the difference
    character_frequencies.append(difference)  # Store the difference in the list

# Step 5: Evaluate Frequencies
has_shortages = 'NO'  # Initialize the variable to check for shortages
if any(freq < 0 for freq in character_frequencies):  # Check for any negative values in the list
    has_shortages = 'YES'  # Set to 'YES' if there are shortages

# Step 6: Output Result
if has_shortages == 'NO':
    print("YES")  # Can form the second string
else:
    print("NO")  # Cannot form the second string
