# Function to process input based on specific substitutions and checks
def process_user_input():
    # Step 2: Read input and remove leading or trailing spaces
    userInput = input().strip()
    
    # Step 3: Replace substrings "dot" with "." and "at" with "@"
    userInput = userInput.replace("dot", ".").replace("at", "@")
    
    # Step 4: Check starting character for "."
    if userInput.startswith('.'):
        userInput = "dot" + userInput[1:]

    # Step 5: Initialize variables
    counter = 0
    charList = []

    # Step 6: Check for starting character "@" and modify the input accordingly
    if userInput.startswith('@'):
        userInput = "at" + userInput[1:]

    # Step 7: Process each character in userInput
    for currentChar in userInput:
        if currentChar == '@':  # Handle "@" symbol specifically
            if counter > 0:
                charList.append("at")
                counter = 1
            else:
                charList.append("@")
                counter = 1
        else:
            charList.append(currentChar)  # Include the current character in the list

    # Step 8: Join characters to form final result
    finalResult = ''.join(charList)

    # Step 9: Check the ending character for "."
    if finalResult.endswith('.'):
        finalResult = finalResult[:-1] + "dot"

    # Step 10: Output the result
    print(finalResult)

# Start the function to process user input
process_user_input()
