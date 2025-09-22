def transformInput():
    # Read a line of input and remove any surrounding whitespace
    line = input().strip()
    
    # Replace occurrences of "dot" with "." and "at" with "@"
    line = line.replace("dot", ".").replace("at", "@")

    # If the first character is ".", prepend "dot" to the string
    if line.startswith("."):
        line = "dot" + line[1:]

    # Initialize variables for processing
    countAtSign = 0
    transformedList = []
    
    # If the first character is "@", prepend "at" to the string
    if line.startswith("@"):
        line = "at" + line[1:]

    # Iterate through each character in the transformed line
    for character in line:
        if character == "@":
            if countAtSign > 0:
                # Replace with "at" to prevent consecutive "at"
                transformedList.append("at")
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
    if finalString.endswith("."):
        finalString = finalString[:-1] + "dot"

    # Output the final transformed string
    print(finalString)

# Testing function with various input scenarios and edge cases
if __name__ == "__main__":
    # Test cases
    inputs = [
        "dot.example@domain.com    ",
        "hello dot world at example.com.",
        "this is a test at test dot.",
        "...",
        "at@at@at.",
        ".leading dot",
        "normal text without replacements"
    ]
    
    for test_input in inputs:
        print(f"Input: {test_input}")
        transformInput()
