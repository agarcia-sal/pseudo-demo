# Function to transform the input string according to specified rules
def transform_input_string():
    # Step 1: Read input
    inputString = input()
    
    # Step 2: Replace keywords "dot" and "at" with "." and "@" respectively
    inputString = inputString.replace("dot", ".").replace("at", "@")
    
    # Step 3: Handle special case for initial character
    if inputString.startswith("."):
        inputString = "dot" + inputString[1:]

    # Step 4: Initialize counter and result list
    atCount = 0
    resultList = []

    # Step 5: Handle special case for email format
    if inputString.startswith("@"):
        inputString = "at" + inputString[1:]

    # Step 6: Process each character in the input string
    for currentChar in inputString:
        if currentChar == "@":
            if atCount > 0:
                # If "@" has occurred before, append "at" to result
                resultList.append("at")
            else:
                # First occurrence of "@"
                resultList.append("@")
            atCount += 1
        else:
            # Append current character to result list
            resultList.append(currentChar)

    # Step 7: Combine results into a single output string
    outputString = ''.join(resultList)

    # Step 8: Handle ending special case
    if outputString.endswith("."):
        outputString = outputString[:-1] + "dot"

    # Step 9: Output the final result
    print(outputString)

# Execute the transformation function
transform_input_string()
