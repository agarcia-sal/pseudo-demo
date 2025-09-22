# Step 1: Read Input
user_input = input()  # Taking a line of input from the user

# Step 2: Initialize Variables
index = 0  # This will serve as the index to traverse the string
result_string = ""  # This string will store the resulting number sequence

# Step 3: Process Each Symbol
while index < len(user_input):  # Loop until we've processed the entire input string
    current_symbol = user_input[index]  # Get the current symbol

    if current_symbol == ".":  # Check if the current symbol is a dot
        result_string += "0"  # Append "0" to the result
        index += 1  # Move to the next symbol

    else:  # If the current symbol is not a dot
        if index + 1 < len(user_input) and user_input[index + 1] == ".":  # Check if the next symbol is also a dot
            result_string += "1"  # Append "1" to the result
            index += 2  # Skip to the next pair of symbols
        else:  # If the next symbol is not a dot
            result_string += "2"  # Append "2" to the result
            index += 2  # Again, skip to the next pair of symbols

# Step 4: Output the Result
print(result_string)  # Print the resulting string of numbers
