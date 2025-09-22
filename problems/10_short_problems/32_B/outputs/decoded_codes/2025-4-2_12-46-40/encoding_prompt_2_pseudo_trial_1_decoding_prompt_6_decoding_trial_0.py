# Step 1: Read input from the user
input_string = input().strip()  # Remove leading/trailing whitespace

# Step 2: Initialize a variable to track the current index
current_index = 0  # This will be used to track our position within input_string

# Step 3: Initialize an empty string to hold the final output
result_string = ""  # This will contain the string of digits generated

# Step 4: Loop through the input string while we haven't reached the end
while current_index < len(input_string):
    # If the current character is a dot
    if input_string[current_index] == '.':
        result_string += '0'  # Append '0' to the result
        current_index += 1  # Move to the next character

    # Otherwise check the next character
    else:
        # Ensure we don't go out of bounds when checking input_string[current_index + 1]
        if current_index + 1 < len(input_string) and input_string[current_index + 1] == '.':
            result_string += '1'  # Append '1' to the result
            current_index += 2  # Move forward by two characters
        else:
            result_string += '2'  # Append '2' to the result
            current_index += 2  # Move forward by two characters

# Step 5: Print the final result
print(result_string)
