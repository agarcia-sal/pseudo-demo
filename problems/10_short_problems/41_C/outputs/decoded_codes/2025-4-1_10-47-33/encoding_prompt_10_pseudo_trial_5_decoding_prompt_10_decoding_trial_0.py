def process_input():
    # Read input and strip leading/trailing whitespace
    input_string = input().strip()
    
    # Replace occurrences of specified substrings
    input_string = input_string.replace("dot", ".")
    input_string = input_string.replace("at", "@")
    
    # Check for leading dot and adjust accordingly
    if input_string and input_string[0] == ".":
        input_string = "dot" + input_string[1:]
    
    # Initialize variables for the processing
    count_at = 0
    result_list = []
    
    # Check for leading at symbol and adjust accordingly
    if input_string and input_string[0] == "@":
        input_string = "at" + input_string[1:]

    # Process each character in the input string
    for char in input_string:
        if char == "@":
            if count_at > 0:
                result_list.append("at")
            else:
                result_list.append("@")
            count_at = 1  # Mark that we've encountered an '@'
        else:
            result_list.append(char)
    
    # Join the processed characters into a final string
    final_string = ''.join(result_list)

    # Check for trailing dot and adjust accordingly
    if final_string and final_string[-1] == ".":
        final_string = final_string[:-1] + "dot"
    
    # Output the final result
    print(final_string)

# Uncomment the following line to run the function and test it directly
# process_input()
