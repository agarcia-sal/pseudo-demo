# This program translates a string of symbols into a numerical string based on specific rules.

# Step 1: Read Input
input_string = input().strip()  # Taking input from the user and stripping any extra whitespace

# Step 2: Initialize Variables
index = 0  # Initialize an index variable to traverse the input string
result_string = ""  # Create an empty string to store the resulting number sequence

# Step 3: Process Each Symbol
while index < len(input_string):  # While the index is less than the length of the input string
    current_symbol = input_string[index]  # Get the current symbol based on the index
    
    if current_symbol == ".":  # Check if the current symbol is a dot
        result_string += "0"  # If it is, append "0" to the result string
        index += 1  # Move to the next symbol (increment the index by 1)
    else:
        # If the current symbol is not a dot, look at the next symbol
        if index + 1 < len(input_string):  # Check to avoid index out of range
            next_symbol = input_string[index + 1]  # Get the next symbol
            
            if next_symbol == ".":  # If the next symbol is a dot
                result_string += "1"  # Append "1" to the result string
                index += 2  # Move to the next pair of symbols (increment the index by 2)
            else:
                result_string += "2"  # If the next symbol is not a dot, append "2" to the result string
                index += 2  # Move to the next pair of symbols (increment the index by 2)
        else:
            # If there's no next symbol, append "2" since we can't form a pair
            result_string += "2"
            index += 1  # Increment index to avoid infinite loop

# Step 4: Output the Result
print(result_string)  # Print the resulting string of numbers
