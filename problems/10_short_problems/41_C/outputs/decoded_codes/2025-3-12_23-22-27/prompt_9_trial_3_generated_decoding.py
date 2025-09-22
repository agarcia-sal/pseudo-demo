# Step 1: Receive Input
input_string = input().strip()  # Read input and remove extra spaces

# Step 2: Replace Keywords
input_string = input_string.replace("dot", ".")
input_string = input_string.replace("at", "@")

# Step 3: Check Starting Character
if input_string and input_string[0] == ".":
    input_string = "dot" + input_string[1:]  # Prepend "dot" if starts with "."

# Step 4: Initialize Variables
count_at = 0
result_list = []  # List to construct final output

# Step 5: Check and Correct Starting Character
if input_string and input_string[0] == "@":
    input_string = "at" + input_string[1:]  # Prepend "at" if starts with "@"

# Step 6: Process Each Character
for character in input_string:
    if character == "@":
        if count_at > 0:
            result_list.append("at")  # Append "at" if "@" has appeared before
        else:
            result_list.append("@")  # Append "@" for the first occurrence
        count_at = 1  # Update count of "@" occurrences
    else:
        result_list.append(character)  # Append other characters directly

# Step 7: Combine the List
final_output = ''.join(result_list)  # Create the final output string

# Step 8: Fix Ending Character
if final_output and final_output[-1] == ".":
    final_output = final_output[:-1] + "dot"  # Replace the last "." with "dot"

# Step 9: Output the Result
print(final_output)  # Print the final formatted output
