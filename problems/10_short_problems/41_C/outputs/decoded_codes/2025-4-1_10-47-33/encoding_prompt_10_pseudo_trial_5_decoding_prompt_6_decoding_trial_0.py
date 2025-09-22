# Step 1: Read input from the user and remove any leading or trailing whitespace
input_string = input().strip()

# Step 2: Replace occurrences of "dot" with "." and "at" with "@"
input_string = input_string.replace("dot", ".").replace("at", "@")

# Step 3: Check for leading dot and modify the string accordingly
if input_string and input_string[0] == ".":
    input_string = "dot" + input_string[1:]

# Step 4: Initialize variables
count_at = 0            # To keep track of consecutive "at" occurrences
result_list = []        # List to gather processed characters

# Step 5: Check for leading at symbol and modify string
if input_string and input_string[0] == "@":
    input_string = "at" + input_string[1:]

# Step 6: Process each character in the input string
for char in input_string:
    if char == "@":  # If the character is the "at" symbol
        if count_at > 0:  # Check for consecutive "at"
            result_list.append("at")  # Append "at" to the result
        else:
            result_list.append("@")  # Append "@" to the result
        count_at = 1  # Set count_at to 1 to indicate we've seen an "at"
    else:
        result_list.append(char)  # Append the character to the result if not "at"
        count_at = 0  # Reset count_at for other characters

# Step 7: Join the results into a single string
final_string = ''.join(result_list)

# Step 8: Check for trailing dot and modify the final string
if final_string and final_string[-1] == ".":
    final_string = final_string[:-1] + "dot"

# Step 9: Output the final result
print(final_string)
