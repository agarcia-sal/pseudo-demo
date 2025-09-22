def process_input_string():
    # Read input and strip leading and trailing whitespace
    input_string = input().strip()
    
    # Replace occurrences of "dot" and "at" with "." and "@"
    input_string = input_string.replace("dot", ".").replace("at", "@")

    # Check for leading period character
    if input_string.startswith("."):
        input_string = "dot" + input_string[1:]

    count_at = 0
    result_list = []

    # Check for leading at character
    if input_string.startswith("@"):
        input_string = "at" + input_string[1:]

    # Process the characters in the input string
    for char in input_string:
        if char == "@":
            if count_at > 0:
                result_list.append("at")
            else:
                result_list.append("@")
            count_at = 1
        else:
            result_list.append(char)

    # Join the result list into a single string
    final_string = ''.join(result_list)

    # Check for trailing period character
    if final_string.endswith("."):
        final_string = final_string[:-1] + "dot"

    # Output the final result
    print(final_string)

# Call the function to execute the process
process_input_string()
