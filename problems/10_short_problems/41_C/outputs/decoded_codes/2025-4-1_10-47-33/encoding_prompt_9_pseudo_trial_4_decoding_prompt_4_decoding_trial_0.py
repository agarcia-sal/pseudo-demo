def transform_email():
    # Step 1: Receive Input
    input_string = input().strip()
    
    # Step 2: Replace Keywords
    modified_string = input_string.replace("dot", ".").replace("at", "@")

    # Step 3: Check Leading Character
    if modified_string.startswith("."):
        modified_string = "dot" + modified_string[1:]

    # Step 4: Initialize the List and Counter
    counter = 0
    processed_chars = []

    # Step 5: Check for Leading "at"
    if modified_string.startswith("@"):
        modified_string = "at" + modified_string[1:]

    # Step 6: Process Each Character
    for char in modified_string:
        if char == "@":
            if counter > 0:
                processed_chars.append("at")
                counter = 1
            else:
                processed_chars.append(char)
                counter = 1
        else:
            processed_chars.append(char)
            counter = 0  # Reset counter for other characters

    # Step 7: Reconstruct the String
    final_string = ''.join(processed_chars)

    # Step 8: Check for Trailing Character
    if final_string.endswith("."):
        final_string = final_string[:-1] + "dot"

    # Step 9: Output the Result
    print(final_string)

# To invoke the function
transform_email()
