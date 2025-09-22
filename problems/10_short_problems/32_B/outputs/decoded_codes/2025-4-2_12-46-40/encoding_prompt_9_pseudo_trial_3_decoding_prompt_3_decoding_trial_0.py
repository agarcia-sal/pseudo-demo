# Function to process input string and convert signals into numerical output
def convert_signals_to_numbers():
    # Step 1: Initialize Input
    inputString = input().strip()  # Read input and remove extra spaces

    # Step 2: Setup Variables
    index = 0  # Track current position in the input string
    outputString = ""  # Initialize the result output string

    # Step 3: Process Input String
    while index < len(inputString):
        if inputString[index] == '.':
            outputString += '0'
            index += 1
        elif index + 1 < len(inputString) and inputString[index + 1] == '.':
            outputString += '1'
            index += 2
        else:
            outputString += '2'
            index += 2

    # Step 4: Output Result
    print(outputString)

# Call the function to execute the conversion
convert_signals_to_numbers()
