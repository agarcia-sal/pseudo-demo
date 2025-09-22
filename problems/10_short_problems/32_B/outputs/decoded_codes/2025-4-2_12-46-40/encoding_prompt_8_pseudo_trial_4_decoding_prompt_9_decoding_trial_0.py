1. Read Input:
   - Get a line of input (a string) and remove any extra spaces or newline characters.
   
2. Initialize Variables:
   - Set an index variable currentPosition to 0 to track our position in the input string.
   - Create an empty string result to store the translated numerical output.
   
3. Process the Input:
   - While currentPosition is less than the length of the input string:
     - If the character at currentPosition is a dot (.):
       - Add 0 to the result.
       - Move currentPosition one step forward.
     - Otherwise, check the next character:
       - If the character after currentPosition is also a dot (.):
         - Add 1 to the result.
         - Move currentPosition forward by two steps.
       - If neither condition is met:
         - Add 2 to the result.
         - Move currentPosition forward by two steps.
    
4. Output the Result:
   - Print the result string which contains the translated numbers.


# Read Input
input_string = input().strip()  # Remove any extra spaces or newline characters

# Initialize Variables
current_position = 0  # To track our position in the input string
result = ""  # To store the translated numerical output

# Process the Input
while current_position < len(input_string):
    if input_string[current_position] == '.':
        result += '0'  # Add 0 to the result for a single dot
        current_position += 1  # Move one step forward
    elif current_position + 1 < len(input_string) and input_string[current_position + 1] == '.':
        result += '1'  # Add 1 to the result for a pair of dots
        current_position += 2  # Move forward by two steps
    else:
        result += '2'  # Add 2 to the result for any other sequence
        current_position += 2  # Move forward by two steps

# Output the Result
print(result)  # Print the translated numerical output
