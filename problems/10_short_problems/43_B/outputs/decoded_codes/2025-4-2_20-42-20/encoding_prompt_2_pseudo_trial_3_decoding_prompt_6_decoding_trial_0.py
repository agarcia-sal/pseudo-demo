# Step 1: Accept input from the user for two strings
string_one = input()  # First string input
string_two = input()  # Second string input

# Step 2: Process the Strings to remove spaces
filtered_string_one = [char for char in string_one if char != ' ']  # List excluding spaces from string_one
filtered_string_two = [char for char in string_two if char != ' ']  # List excluding spaces from string_two

# Step 3: Count Character Frequencies
frequency_difference = []  # List to keep track of frequency differences

# Calculate the frequency for each character using ASCII values
for ascii_value in range(ord('A'), ord('z') + 1):
    # Convert ASCII value to corresponding character
    char = chr(ascii_value)  
    count_one = filtered_string_one.count(char)  # Count in filtered_string_one
    count_two = filtered_string_two.count(char)  # Count in filtered_string_two
    difference = count_one - count_two  # Calculate the frequency difference
    frequency_difference.append(difference)  # Append the difference to the list

# Step 4: Check Frequency Conditions
negative_counts = [count for count in frequency_difference if count < 0]  # List of negative counts

# Determine the result based on whether negative counts are present
if not negative_counts:  # If the list of negative counts is empty
    result = "YES"
else:
    result = "NO"

# Step 5: Output the result
print(result)  # Display the final result
