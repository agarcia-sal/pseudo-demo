# Function to process the email-like input string
def process_email_input():
    # Step 1: Read Input
    emailInput = input().strip()  # Obtain input and strip leading/trailing whitespace

    # Step 2: Replace Substrings
    emailInput = emailInput.replace("dot", ".")  # Replace 'dot' with '.'
    emailInput = emailInput.replace("at", "@")    # Replace 'at' with '@'

    # Step 3: Ensure Starting Character Rule
    if emailInput.startswith('.'):
        emailInput = "dot" + emailInput  # Prepend 'dot' if input starts with '.'

    # Step 4: Initialize State Variables
    previousAtCount = 0
    outputCharacters = []  # List to hold processed characters

    # Step 5: Handle the '@' Character
    if emailInput.startswith('@'):
        emailInput = "at" + emailInput[1:]  # Replace first '@' with 'at'

    # Step 6: Process Each Character in the String
    for currentCharacter in emailInput:
        if currentCharacter == '@':
            if previousAtCount > 0:
                outputCharacters.append("at")  # Append 'at' if there's a previous '@'
                previousAtCount = 1  # Update count
            else:
                outputCharacters.append('@')  # Append first '@'
                previousAtCount = 1  # Mark first '@'
        else:
            outputCharacters.append(currentCharacter)  # Append normal characters

    # Step 7: Form the Final Output String
    finalOutput = ''.join(outputCharacters)  # Join characters to form final string
    if finalOutput.endswith('.'):
        finalOutput = finalOutput[:-1] + "dot"  # Replace last '.' with 'dot'

    # Step 8: Display the Result
    print(finalOutput)  # Output the final processed string

# Entry point of the script
if __name__ == "__main__":
    process_email_input()  # Call the function to execute the email processing
