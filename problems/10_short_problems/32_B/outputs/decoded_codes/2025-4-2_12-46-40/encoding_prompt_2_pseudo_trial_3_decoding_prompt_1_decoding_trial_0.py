# Step 1: Read a string of characters representing a sequence of symbols
input_string = input()  # Read the input string

# Step 2: Initialize an index variable and an empty result string
index = 0
result = ''  # This will hold the final output digits

# Step 3: While the index is less than the length of the input string
while index < len(input_string):
    current_symbol = input_string[index]  # Get the current symbol
    
    # Step 3a: Check if the current symbol is a dot
    if current_symbol == '.':
        result += '0'  # Append '0' to the result
        index += 1  # Move to the next symbol
    
    # Step 3b: Check if the next symbol is also a dot
    elif index + 1 < len(input_string) and input_string[index + 1] == '.':
        result += '1'  # Append '1' to the result
        index += 2  # Move forward by two positions
    
    # Step 3c: Then the current symbol must be a dash followed by a dot
    elif index + 1 < len(input_string) and input_string[index + 1] != '.':
        result += '2'  # Append '2' to the result
        index += 2  # Move forward by two positions

# Step 4: Output the final result string
print(result)
