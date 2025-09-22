# Start the main process

# Step 2: Read a line of input from the user
input_string_1 = input()
input_string_2 = input()

# Step 4: Split the input strings into lists of tokens
tokens_1 = input_string_1.split()
tokens_2 = input_string_2.split()

# Step 6: Initialize a counter for differences
difference_count = 0

# Step 7: Check the first three entries of both lists
for index in range(3):
    # Convert the current entry in both tokens to integers
    value_from_first_input = int(tokens_1[index])
    value_from_second_input = int(tokens_2[index])
    
    # Check for differences
    if value_from_first_input != value_from_second_input:
        difference_count += 1

# Step 8 and 9: Output based on the number of differences
if difference_count < 3:
    print("YES")  # Fewer than three differences
else:
    print("NO")   # Three or more differences
