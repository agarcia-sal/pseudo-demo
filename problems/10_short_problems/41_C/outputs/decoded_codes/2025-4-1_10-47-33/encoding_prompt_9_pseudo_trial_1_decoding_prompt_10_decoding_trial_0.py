def transform_email_string():
    # Step 1: Receive input from the user
    email_like_string = input().strip()
    
    # Step 2: Replace word aliases
    email_like_string = email_like_string.replace("dot", ".").replace("at", "@")

    # Step 3: Adjust beginning of string
    if email_like_string.startswith("."):
        email_like_string = "dot" + email_like_string

    # Step 4: Initialize counters and list
    at_counter = 0
    modified_characters = []
    
    # Step 5: Handle special cases for starting character
    if email_like_string.startswith("@"):
        modified_characters.append("at")
        at_counter += 1
    else:
        for char in email_like_string:
            # Step 6: Iterate through each character
            if char == "@":
                if at_counter > 0:
                    modified_characters.append("at")
                else:
                    modified_characters.append("@")
                at_counter += 1
            else:
                modified_characters.append(char)

    # Step 7: Combine list into string
    result_string = ''.join(modified_characters)

    # Step 8: Adjust end of string
    if result_string.endswith("."):
        result_string = result_string[:-1] + "dot"
    
    # Step 9: Output modified string
    print(result_string)

# Example usage:
transform_email_string()
