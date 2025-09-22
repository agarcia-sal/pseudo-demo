def process_input():
    # Step 1: Receive input
    user_input = input().strip()
    
    # Step 2: Replace specific strings
    user_input = user_input.replace("dot", ".")
    user_input = user_input.replace("at", "@")
    
    # Step 3: Check beginning of string
    if user_input and user_input[0] == ".":
        user_input = "dot" + user_input[1:]
    
    # Step 4: Initialize variables
    at_counter = 0
    collected_chars = []
    
    # Step 5: Handle starting character
    if user_input and user_input[0] == "@":
        collected_chars.append("at")
        at_counter += 1
        collected_chars.append(user_input[1:])
    else:
        collected_chars.append(user_input)
    
    # Step 6: Iterate through characters
    for char in collected_chars[0]:
        if char == "@":
            if at_counter > 0:  # Previous occurrence of "at" detected
                collected_chars.append("at")
            else:  # First occurrence of "@" detected
                collected_chars = ["@"]  # Start fresh with "@" indication
            at_counter += 1  # Increment the "at" occurrences count
        else:
            if len(collected_chars) == 1 and collected_chars[0] == "@":
                collected_chars[0] = char  # Replace initial "@" placeholder
            else:
                collected_chars.append(char)

    # Step 7: Combine collected characters into a single string
    final_string = ''.join(collected_chars)
    
    # Step 8: Final adjustment
    if final_string and final_string[-1] == ".":
        final_string = final_string[:-1] + "dot"
    
    # Step 9: Output the result
    print(final_string)

# Run the function
process_input()
