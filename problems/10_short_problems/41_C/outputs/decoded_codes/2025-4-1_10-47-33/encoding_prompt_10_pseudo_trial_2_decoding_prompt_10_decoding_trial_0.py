def process_input():
    # Step 1: Read Input
    input_string = input().strip()

    # Step 2: Replace Substrings
    input_string = input_string.replace("dot", ".").replace("at", "@")
    
    # Step 3: Check Starting Character
    if input_string and input_string[0] == '.':
        input_string = "dot" + input_string[1:]

    # Step 4: Initialize Variables
    count_at = 0
    result_list = []

    # Step 5: Handle Starting Character for @
    if input_string and input_string[0] == '@':
        result_list.append("at")
        count_at = 1

    # Step 6: Process Each Character
    for character in input_string:
        if character == '@':
            if count_at > 0:
                result_list.append("at")
            else:
                result_list.append('@')
            count_at += 1
        else:
            result_list.append(character)
            count_at = 0  # Reset count for other characters

    # Step 7: Join Result
    processed_string = ''.join(result_list)

    # Step 8: Check Ending Character
    if processed_string and processed_string[-1] == '.':
        processed_string = processed_string[:-1] + "dot"

    # Step 9: Output the Result
    print(processed_string)

# To test the function, you may call process_input()
