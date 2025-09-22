def transform_input():
    # Read a line of input from standard input and strip surrounding whitespace
    line = input().strip()
    
    # Replace occurrences of "dot" with "." and "at" with "@"
    line = line.replace("dot", ".").replace("at", "@")

    # If the first character is ".", prepend "dot"
    if line and line[0] == '.':
        line = "dot" + line[1:]

    # Initialize variables for further processing
    count_at_sign = 0
    transformed_list = []
    
    # If the first character is "@", prepend "at"
    if line and line[0] == '@':
        line = "at" + line[1:]

    # Iterate through each character in the transformed line
    for char in line:
        if char == '@':
            if count_at_sign > 0:
                # Replace consecutive "@" with "at"
                transformed_list.append("at")
            else:
                # First occurrence of "@"
                transformed_list.append(char)
                count_at_sign += 1
        else:
            # Append the current character as is
            transformed_list.append(char)

    # Join the transformed list into a single string
    final_string = ''.join(transformed_list)

    # If the last character is ".", replace it with "dot"
    if final_string and final_string[-1] == '.':
        final_string = final_string[:-1] + "dot"

    # Output the final transformed string
    print(final_string)
