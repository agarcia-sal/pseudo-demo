# Step 1: Retrieve Input
first_string = input()  # Get the first string from the user
second_string = input()  # Get the second string from the user

# Step 2: Preprocess Input
cleaned_strings = [
    first_string.replace(" ", ""),  # Remove spaces from first_string
    second_string.replace(" ", "")   # Remove spaces from second_string
]
s1 = cleaned_strings[0]  # Assign the cleaned version of first_string
s2 = cleaned_strings[1]  # Assign the cleaned version of second_string

# Step 3: Count Character Frequencies
frequency_difference = []  # Initialize a list to store differences in character counts

# ASCII 65 to 122 corresponds to characters A-Z and a-z
for char in range(65, 123):
    char_count_s1 = s1.count(chr(char))  # Count occurrences in s1
    char_count_s2 = s2.count(chr(char))  # Count occurrences in s2
    difference = char_count_s1 - char_count_s2  # Calculate the difference
    frequency_difference.append(difference)  # Append the difference to the list

# Step 4: Check Character Count Requirements
negative_count = sum(1 for count in frequency_difference if count < 0)  # Count negative differences

# Step 5: Provide Output
if negative_count == 0:  # If there are no negative differences
    print("YES")  # Transformation is possible
else:
    print("NO")  # Transformation is not possible
