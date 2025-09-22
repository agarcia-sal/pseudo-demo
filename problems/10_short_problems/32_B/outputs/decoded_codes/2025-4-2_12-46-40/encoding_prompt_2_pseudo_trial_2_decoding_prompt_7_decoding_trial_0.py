# Function to decode the input string according to specific rules
def decode_string():
    # Step 1: Read a line of input containing encoded information
    input_string = input()
    
    # Step 2: Initialize variables
    currentIndex = 0  # Index tracker for the input string
    outputString = ""  # Variable to store the resulting output

    # Step 3: Processing loop
    while currentIndex < len(input_string):
        # Check the character at the current index
        if input_string[currentIndex] == '.':
            outputString += '0'  # Append '0' to the output string
            currentIndex += 1     # Move to the next character
        elif (currentIndex + 1 < len(input_string) and 
              input_string[currentIndex + 1] == '.'):
            outputString += '1'  # Append '1' to the output string
            currentIndex += 2     # Skip the next character
        else:
            outputString += '2'  # Append '2' to the output string
            currentIndex += 2     # Skip the next character

    # Step 4: Output the resulting string
    print(outputString)

# Call the decode function to execute the transformation
decode_string()
