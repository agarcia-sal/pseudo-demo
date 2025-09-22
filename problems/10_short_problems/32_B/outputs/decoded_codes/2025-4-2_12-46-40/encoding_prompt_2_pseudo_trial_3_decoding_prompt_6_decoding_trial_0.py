# Step 1: Read the input string of symbols
input_string = input()

# Step 2: Initialize index and result string
index = 0
result_string = ""

# Step 3: Process the input string while there are more symbols
while index < len(input_string):
    current_symbol = input_string[index]  # Get the current symbol

    # Check if the current symbol is a dot
    if current_symbol == '.':
        result_string += '0'  # Append '0' for a single dot
        index += 1  # Move to the next symbol

    # Check if the next symbol exists and is also a dot
    elif index + 1 < len(input_string) and input_string[index + 1] == '.':
        result_string += '1'  # Append '1' for two dots
        index += 2  # Move past both symbols

    # Otherwise, we expect a dash followed by a dot
    else:
        result_string += '2'  # Append '2' for a dash-dot pair
        index += 2  # Move past both symbols

# Step 4: Print the final result string
print(result_string)
