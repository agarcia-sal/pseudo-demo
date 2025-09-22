# Begin the program
def main():
    # Step 1: Read the input string and prepare it for processing
    inputString = input().strip()  # Reading the input and removing whitespace

    # Step 2: Replace specific substrings for formatting
    inputString = inputString.replace("dot", ".")
    inputString = inputString.replace("at", "@")

    # Step 3: Check and modify the first character if it's a period
    if inputString and inputString[0] == ".":  # Check if the string is not empty
        inputString = "dot" + inputString[1:]  # Prepend "dot" to the inputString

    # Step 4: Initialize variables for processing the string
    countAt = 0  # Counter for occurrences of '@' character
    formattedCharacters = []  # List to hold processed characters

    # Step 5: Modify the string further if it starts with '@'
    if inputString and inputString[0] == "@":  # Check if the string is not empty
        inputString = "at" + inputString[1:]  # Prepend "at" to the inputString

    # Step 6: Iterate through each character in the modified string
    for character in inputString:
        if character == "@":
            if countAt > 0:  # Check if '@' has been encountered before
                formattedCharacters.append("at")
                countAt = 1  # Reset the count to 1 to avoid duplicates
            else:
                formattedCharacters.append(character)
                countAt = 1  # Increment the count
        else:
            formattedCharacters.append(character)

    # Step 7: Join the formatted characters into a single string
    outputString = ''.join(formattedCharacters)

    # Step 8: Final formatting for the output string
    if outputString and outputString[-1] == ".":  # Check if string is not empty
        outputString = outputString[:-1] + "dot"  # Replace the last '.' with 'dot'

    # Step 9: Output the final formatted string
    print(outputString)  # Print the final result

# Call the main function to execute the program
if __name__ == "__main__":
    main()
