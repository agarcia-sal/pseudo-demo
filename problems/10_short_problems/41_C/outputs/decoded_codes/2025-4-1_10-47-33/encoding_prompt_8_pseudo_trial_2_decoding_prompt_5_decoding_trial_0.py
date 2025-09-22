# Function to format an email-like string by replacing keywords and adjusting characters
def format_email_string():
    # Step 1: Read input and remove surrounding whitespace
    emailString = input().strip()
    
    # Step 2: Replace keywords "dot" and "at"
    emailString = emailString.replace("dot", ".")
    emailString = emailString.replace("at", "@")
    
    # Step 3: Handle leading period
    if emailString.startswith("."):
        emailString = "dot" + emailString[1:]
    
    # Step 4: Check for leading "at" symbol
    if emailString.startswith("@"):
        emailString = "at" + emailString[1:]

    # Step 5: Initialize counter and list for formatted characters
    counter = 0
    formattedCharacters = []
    
    # Step 6: Process each character
    for character in emailString:
        if character == "@":
            if counter > 0:
                formattedCharacters.append("at")
                counter = 1
            else:
                formattedCharacters.append("@")
                counter = 1
        else:
            formattedCharacters.append(character)
    
    # Step 7: Join characters into a final string
    finalString = ''.join(formattedCharacters)
    
    # Step 8: Handle trailing period
    if finalString.endswith("."):
        finalString = finalString[:-1] + "dot"

    # Step 9: Output the result
    print(finalString)

# Example test case (can be removed during actual runs):
# Input: "example dot com"
# Output: "example.com"
