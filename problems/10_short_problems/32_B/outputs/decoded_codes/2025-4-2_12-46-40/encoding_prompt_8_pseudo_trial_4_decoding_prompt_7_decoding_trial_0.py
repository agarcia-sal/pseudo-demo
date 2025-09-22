# Purpose: Translate a string of characters (dot and dash encoding) into a numerical string

# Read Input
input_string = input().strip()  # Get a line of input and remove extra spaces or newline characters

# Initialize Variables
currentPosition = 0  # Index variable to track our position in the input string
result = ""  # String to store the translated numerical output

# Process the Input
while currentPosition < len(input_string):  # While we haven't reached the end of the input string
    if input_string[currentPosition] == '.':  # Check if the current character is a dot
        result += '0'  # Add '0' to the result
        currentPosition += 1  # Move forward by one step
    else:  # If the current character is not a dot (implying it's a dash)
        if currentPosition + 1 < len(input_string) and input_string[currentPosition + 1] == '.':
            result += '1'  # Add '1' if the next character is also a dot
            currentPosition += 2  # Move forward by two steps
        else:
            result += '2'  # Add '2' if we don't find another dot next
            currentPosition += 2  # Move forward by two steps

# Output the Result
print(result)  # Print the translated numbers
