# Step 1: Receive Input
input_string = input().strip()  # Read input from the user and remove extra spaces

# Step 2: Replace Keywords
input_string = input_string.replace("dot", ".")  # Replace 'dot' with '.'
input_string = input_string.replace("at", "@")    # Replace 'at' with '@'

# Step 3: Check Starting Character
if input_string.startswith("."):
    input_string = "dot" + input_string[1:]  # Prepend 'dot' if starting with '.'

# Step 4: Initialize Variables
count_at = 0  # To count occurrences of '@'
result_list = []  # To construct the final output

# Step 5: Check and Correct Starting Character
if input_string.startswith("@"):
    input_string = "at" + input_string[1:]  # Prepend 'at' if starting with '@'

# Step 6: Process Each Character
for character in input_string:
    if character == "@":  # Check for '@'
        if count_at > 0:
            result_list.append("at")  # Append 'at' if '@' has appeared before
        else:
            result_list.append("@")  # Append '@' once
            count_at = 1  # Set count at to 1
    else:
        result_list.append(character)  # Append regular characters

# Step 7: Combine the List
final_output = ''.join(result_list)  # Create the final output string

# Step 8: Fix Ending Character
if final_output.endswith("."):  # Check if output ends with '.'
    final_output = final_output[:-1] + "dot"  # Replace '.' with 'dot'

# Step 9: Output the Result
print(final_output)  # Print the final output
