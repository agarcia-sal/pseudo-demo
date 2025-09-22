def process_input():
    # Step 1: Read input and remove leading/trailing whitespace
    input_string = input().strip()

    # Step 2: Replace "dot" with "."
    modified_string = input_string.replace("dot", ".")

    # Step 3: Replace "at" with "@"
    modified_string = modified_string.replace("at", "@")

    # Step 4: Check if the first character is a period
    if modified_string and modified_string[0] == '.':
        modified_string = "dot" + modified_string[1:]

    # Step 5: Initialize counter and list to hold characters
    at_counter = 0
    result_list = []

    # Step 6: Check if the first character is an "at" symbol
    if modified_string and modified_string[0] == '@':
        result_list.append("at")
        at_counter += 1
        modified_string = modified_string[1:]  # Exclude '@' from further processing

    # Step 8: Process each character in the modified string
    for char in modified_string:
        if char == '@':
            if at_counter > 0:
                result_list.append("at")
                at_counter = 1  # Incrementing to ensure only one instance of "at" is added
            else:
                result_list.append('@')
                at_counter = 1
        else:
            at_counter = 0  # Reset the counter if the character is not '@'
            result_list.append(char)

    # Step 9: Join all elements in the list to form a single string
    final_string = ''.join(result_list)

    # Step 10: Check if the last character is a period
    if final_string and final_string[-1] == '.':
        final_string = final_string[:-1] + "dot"

    # Step 11: Output the modified string
    print(final_string)

# Call the function to execute the input processing
process_input()
