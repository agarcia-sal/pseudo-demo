def transform_email():
    # Step 1: Receive input and clean it
    raw_email = input().strip()

    # Step 2: Replace "dot" with "." and "at" with "@"
    modified_email = raw_email.replace("dot", ".").replace("at", "@")

    # Step 3: Check and handle leading character for formatting
    if modified_email.startswith("."):
        modified_email = "dot" + modified_email[1:]

    # Step 4: Initialize the list and counter
    counter = 0
    processed_chars = []

    # Step 5: Check for leading "at"
    if modified_email.startswith("@"):
        processed_chars.append("at")
        modified_email = modified_email[1:]

    # Step 6: Process each character in the modified email
    for char in modified_email:
        if char == "@":
            if counter > 0:
                processed_chars.append("at")
                counter = 1
            else:
                processed_chars.append(char)
                counter = 1
        else:
            processed_chars.append(char)

    # Step 7: Reconstruct the string
    final_email = ''.join(processed_chars)

    # Step 8: Check and handle trailing character
    if final_email.endswith("."):
        final_email = final_email[:-1] + "dot"

    # Step 9: Output the result
    print(final_email)

# Call the function to execute
transform_email()
