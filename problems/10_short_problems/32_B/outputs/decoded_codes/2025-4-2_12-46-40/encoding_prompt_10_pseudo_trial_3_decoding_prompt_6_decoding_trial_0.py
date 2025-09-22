# Initialize variables by reading input
input_string = input().strip()  # Read input and remove trailing spaces
index = 0  # Start index for processing
answer = ""  # Initialize an empty string to hold the result

# Process each character in the input string
while index < len(input_string):  # Continue while there are characters left to process
    if input_string[index] == '.':  # Check if the current character is '.'
        answer += '0'  # Append '0' to the answer
        index += 1  # Move to the next character
    elif index + 1 < len(input_string) and input_string[index + 1] == '.':  # Check the next character
        answer += '1'  # Append '1' to the answer
        index += 2  # Move past the current and next character
    else:  # If the current character is neither '.' nor the next character is '.'
        answer += '2'  # Append '2' to the answer
        index += 2  # Move past the current and next character
    
# Output the result
print(answer)  # Print the final transformed string
