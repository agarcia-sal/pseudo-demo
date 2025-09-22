def transformInput():
    # Read a line of input and remove any surrounding whitespace
    line = input().strip()
    
    # Replace occurrences of "dot" with "." and "at" with "@"
    line = line.replace("dot", ".").replace("at", "@")
    
    # If the first character is ".", prepend "dot" to the string
    if line and line[0] == ".":
        line = "dot" + line[1:]
    
    # Initialize variables for processing
    countAtSign = 0
    transformedList = []
    
    # If the first character is "@", prepend "at" to the string
    if line and line[0] == "@":
        line = "at" + line[1:]

    # Iterate through each character in the transformed line
    for character in line:
        if character == "@":
            if countAtSign > 0:
                # Replace with "at" to prevent consecutive "at"
                transformedList.append("at")
                countAtSign = 1
            else:
                # First occurrence of "@"
                transformedList.append("@")
                countAtSign = 1
        else:
            # Append the current character as is
            transformedList.append(character)

    # Join the transformed list into a single string
    finalString = ''.join(transformedList)

    # If the last character is ".", replace it with "dot"
    if finalString and finalString[-1] == ".":
        finalString = finalString[:-1] + "dot"

    # Output the final transformed string
    print(finalString)
