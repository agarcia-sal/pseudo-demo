# Function to process user input and replace substrings accordingly
def process_input():
    # Read input from the user and trim leading/trailing spaces
    userInput = input().strip()
    
    # Replace occurrences of "dot" with "."
    userInput = userInput.replace("dot", ".")
    # Replace occurrences of "at" with "@"
    userInput = userInput.replace("at", "@")
    
    # Check if the first character is a dot and prepend "dot" if necessary
    if userInput.startswith("."):
        userInput = "dot" + userInput[1:]

    # Initialize a counter for "@" symbols and list to hold processed characters
    counter = 0
    charList = []

    # Check if the first character is "@" and prepend "at" if necessary
    if userInput.startswith("@"):
        userInput = "at" + userInput[1:]

    # Process each character in the modified userInput
    for currentChar in userInput:
        if currentChar == "@":
            if counter > 0:
                # Append "at" if "@" was already encountered
                charList.append("at")
                counter = 1
            else:
                # Append "@" only once and set counter
                charList.append("@")
                counter = 1
        else:
            # Append the current character to the list
            charList.append(currentChar)

    # Join characters to create the final result string
    finalResult = ''.join(charList)
    
    # Check if the last character is a dot and update finalResult accordingly
    if finalResult.endswith("."):
        finalResult = finalResult[:-1] + "dot"

    # Output the final result
    print(finalResult)

# Uncomment the following line to run the function
# process_input()
