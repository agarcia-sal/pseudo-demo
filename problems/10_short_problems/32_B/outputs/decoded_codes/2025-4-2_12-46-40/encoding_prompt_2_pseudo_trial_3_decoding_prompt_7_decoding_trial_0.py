# This Python code translates the given pseudocode into a working program
# that reads a string of symbols and produces a corresponding string of digits.

# Step 1: Read input from the standard input
input_string = input()  # Read the symbolic input sequence

# Step 2: Initialize an index variable and an empty result string
index = 0
result = ""

# Step 3: Process the input string based on the defined patterns
while index < len(input_string):  # Loop until the end of the string
    current_symbol = input_string[index]  # Get the current symbol
    
    if current_symbol == '.':  # Check if the current symbol is a dot
        result += '0'  # Append '0' for a single dot
        index += 1  # Move to the next symbol
        
    elif (index + 1 < len(input_string) and  # Check for next symbol to avoid index error
          input_string[index + 1] == '.'):  # Check if next symbol is also a dot
        result += '1'  # Append '1' for a pair of dots
        index += 2  # Move forward by two symbols
        
    elif (index + 1 < len(input_string) and  # Ensure there's a next symbol
          input_string[index + 1] == '-'):  # Check if the next symbol is a dash
        result += '2'  # Append '2' for dash followed by a dot
        index += 2  # Move forward by two symbols
    
# Step 4: Output the final result string
print(result)  # Print the constructed string of digits
