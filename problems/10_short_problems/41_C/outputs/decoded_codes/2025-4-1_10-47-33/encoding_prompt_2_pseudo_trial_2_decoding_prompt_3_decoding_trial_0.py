def process_input_string():
    # Step 1: Receive Input
    input_string = input().strip()
    
    # Step 2: Replace Specific Strings
    modified_string = input_string.replace("dot", ".").replace("at", "@")

    # Step 3: Check Beginning of String
    if modified_string.startswith("."):
        modified_string = "dot" + modified_string[1:]

    # Step 4: Initialize Variables
    at_counter = 0
    collected_characters = []
    
    # Step 5: Handle Starting Character
    if modified_string.startswith("@"):
        modified_string = "at" + modified_string[1:]

    # Step 6: Iterate Through Characters
    for char in modified_string:
        if char == "@":
            if at_counter > 0:
                collected_characters.append("at")
            else:
                collected_characters.append(char)
            at_counter += 1
        else:
            collected_characters.append(char)

    # Step 7: Combine Collected Characters
    final_string = ''.join(collected_characters)

    # Step 8: Final Adjustment
    if final_string.endswith("."):
        final_string = final_string[:-1] + "dot"
    
    # Step 9: Output the Result
    print(final_string)

# Here you can call the function to test it
process_input_string()
