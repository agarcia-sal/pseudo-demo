def process_input():
    # Step 2: Read Input
    user_input = input().strip()

    # Step 3: Replace Substrings
    user_input = user_input.replace("dot", ".").replace("at", "@")

    # Step 4: Check Beginning Character
    if user_input.startswith('.'):
        user_input = "dot" + user_input[1:]  # Prepend "dot" and remove leading dot
    
    # Step 5: Initialize Variables
    char_list = []
    counter = 0
    
    # Step 6: Check for Starting Character
    if user_input.startswith('@'):
        user_input = "at" + user_input[1:]  # Prepend "at" and remove leading "@"

    # Step 7: Process Each Character
    for current_char in user_input:
        if current_char == '@':
            # If already seen an "@" character
            if counter > 0:
                char_list.append("at")
            else:
                char_list.append(current_char)  # Append "@" itself
            counter = 1
        else:
            char_list.append(current_char)  # Append the current character

    # Step 8: Join Characters
    final_result = ''.join(char_list)

    # Step 9: Check Ending Character
    if final_result.endswith('.'):
        final_result = final_result[:-1] + "dot"  # Remove last character and append "dot"

    # Step 10: Output Result
    print(final_result)

# Invoke the function to start processing input
process_input()
