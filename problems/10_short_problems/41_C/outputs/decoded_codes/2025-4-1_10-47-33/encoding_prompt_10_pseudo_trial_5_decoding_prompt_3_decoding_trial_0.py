def transform_string():
    # Step 1: Read input from standard input
    input_string = input().strip()

    # Step 2: Replace substrings "dot" with "." and "at" with "@"
    input_string = input_string.replace("dot", ".")
    input_string = input_string.replace("at", "@")
    
    # Step 3: Check and handle leading dot
    if input_string.startswith("."):
        input_string = "dot" + input_string[1:]

    # Step 4: Initialize counter and result list
    count_at = 0
    result_list = []

    # Step 5: Check and handle leading at symbol
    if input_string.startswith("@"):
        input_string = "at" + input_string[1:]

    # Step 6: Process each character in input_string
    for char in input_string:
        if char == "@":
            if count_at > 0:
                result_list.append("at")
            else:
                result_list.append("@")
            count_at = 1
        else:
            result_list.append(char)

    # Step 7: Join results into a final string
    final_string = ''.join(result_list)

    # Step 8: Check and handle trailing dot
    if final_string.endswith('.'):
        final_string = final_string[:-1] + "dot"

    # Step 9: Output the final result
    print(final_string)

# Call the function to run the transformation
transform_string()
