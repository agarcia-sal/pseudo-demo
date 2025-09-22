# Function to transform an email-like string
def transform_email():
    # Step 1: Receive Input
    email_string = input().strip()  # Read input and remove surrounding whitespace
    
    # Step 2: Replace Text Patterns
    email_string = email_string.replace("dot", ".").replace("at", "@")
    
    # Step 3: Adjust Leading Character
    if email_string.startswith("."):
        email_string = "dot" + email_string
    
    # Step 4: Initialize Variables
    at_counter = 0  # Counter to track occurrences of "@"
    transformed_characters = []  # List to store characters for reconstruction
    
    # Step 5: Check for Leading "at"
    if email_string.startswith("@"):
        email_string = "at" + email_string
    
    # Step 6: Iterate Through Each Character
    for character in email_string:
        if character == "@":
            if at_counter > 0:  # Already encountered "@" once
                transformed_characters.append("at")
                at_counter = 1  # Reset counter
            else:
                transformed_characters.append("@")
                at_counter = 1  # Increment counter
        else:
            transformed_characters.append(character)  # Append non-"@" character
    
    # Step 7: Reconstruct the String
    transformed_string = ''.join(transformed_characters)
    
    # Step 8: Adjust Trailing Character
    if transformed_string.endswith("."):
        transformed_string = transformed_string[:-1] + "dot"  # Replace trailing "." with "dot"
    
    # Step 9: Output the Result
    print(transformed_string)

# Example test cases (uncomment to test):
# Input: "my email is user dot example at gmail dot com"
# Output: "my email is user@example.com"
# Input: "dotexample"
# Output: "dotexample"
# Input: "atuser"
# Output: "atuser"
