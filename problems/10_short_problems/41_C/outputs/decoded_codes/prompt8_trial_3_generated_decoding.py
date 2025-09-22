def FormatEmailString():
    # Step 1: Read Input
    originalString = input().strip()
    
    # Step 2: Replace Keywords
    originalString = originalString.replace("dot", ".").replace("at", "@")
    
    # Step 3: Check First Character
    if originalString and originalString[0] == ".":
        originalString = "dot" + originalString
    
    # Step 4: Initialize Variables
    counter = 0
    resultList = []
    
    # Step 5: Format Characters
    for currentCharacter in originalString:
        if currentCharacter == "@":
            if counter > 0:
                resultList.append("at")
                counter = 1
            else:
                resultList.append("@")
                counter = 1
        else:
            resultList.append(currentCharacter)
            counter = 0
    
    # Step 6: Construct the Final String
    finalString = ''.join(resultList)
    
    # Step 7: Check Last Character
    if finalString and finalString[-1] == ".":
        finalString = finalString[:-1] + "dot"
    
    # Step 8: Print the Result
    print(finalString)

# You can call the function by simply using:
# FormatEmailString()
