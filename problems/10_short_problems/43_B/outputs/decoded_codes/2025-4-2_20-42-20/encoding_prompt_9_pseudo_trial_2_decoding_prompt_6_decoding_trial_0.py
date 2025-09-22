# Step 1: Input Strings
first_string = input()  # Receive the first string from the user
second_string = input()  # Receive the second string from the user

# Step 2: Process Input - Remove spaces from both strings
first_string = first_string.replace(" ", "")
second_string = second_string.replace(" ", "")

# Step 3: Initialize Frequency Count
# We will use a list to hold the count of character differences for ASCII values
character_differences = [0] * 128  # Assuming ASCII characters

# Count character occurrences in first_string
for char in first_string:
    character_differences[ord(char)] += 1  # Increment count for this character

# Subtract character occurrences found in second_string
for char in second_string:
    character_differences[ord(char)] -= 1  # Decrement count for this character

# Step 4: Check Feasibility
negative_count = 0  # Counter for negative values in character_differences

# Count how many values in character_differences are negative
for difference in character_differences:
    if difference < 0:
        negative_count += 1

# Step 5: Output the Result
if negative_count > 0:
    print("NO")  # If there are any negative differences, print NO
else:
    print("YES")  # If all differences are non-negative, print YES
