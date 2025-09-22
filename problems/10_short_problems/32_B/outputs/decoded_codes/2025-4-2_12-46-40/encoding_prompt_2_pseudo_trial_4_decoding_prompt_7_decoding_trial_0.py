# Step 1: Read input.
input_string = input().strip()  # Trim leading and trailing whitespace

# Step 2: Initialization
currentIndex = 0  # Initialize index tracker
outputString = ""  # Initialize output string

# Step 3: Process Loop
while currentIndex < len(input_string):  # Loop until the end of the string
    if input_string[currentIndex] == '.':  # Check if current character is a dot
        outputString += '0'  # Append '0' to output string
        currentIndex += 1  # Move to the next character
    else:  # If the current character is not a dot
        if currentIndex + 1 < len(input_string) and input_string[currentIndex + 1] == '.':  # Check next character
            outputString += '1'  # Append '1' to output string
            currentIndex += 2  # Move to the next two characters
        else:  # If next character is not a dot
            outputString += '2'  # Append '2' to output string
            currentIndex += 2  # Move to the next two characters

# Step 4: Output the result
print(outputString)  # Print the final transformed output string
