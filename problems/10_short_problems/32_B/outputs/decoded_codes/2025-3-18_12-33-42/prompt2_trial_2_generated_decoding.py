# Step 1: Read a line of input, which is a string consisting of characters.
input_string = input()

# Step 2: Initialize variables.
index = 0  # Index variable to track the current position in the string
result_string = ""  # Empty string to hold the result of the translation

# Step 3: Process the input.
while index < len(input_string):
    if input_string[index] == '.':
        result_string += '0'  # Append '0' to the result string
        index += 1  # Move the index forward by one position
    else:
        # Check the next character
        if index + 1 < len(input_string) and input_string[index + 1] == '.':
            result_string += '1'  # Append '1' to the result string
            index += 2  # Move the index forward by two positions
        else:
            result_string += '2'  # Append '2' to the result string
            index += 2  # Move the index forward by two positions

# Step 4: Output the resulting translated string.
print(result_string)
