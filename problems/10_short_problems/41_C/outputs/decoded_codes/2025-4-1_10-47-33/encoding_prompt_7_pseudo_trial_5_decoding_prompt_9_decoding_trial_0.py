def transform_input():
    # Read a line of input and remove any surrounding whitespace
    line = input().strip()
    
    # Replace occurrences of "dot" with "." and "at" with "@"
    line = line.replace("dot", ".")
    line = line.replace("at", "@")

    # If the first character is ".", prepend "dot" to the string
    if line.startswith('.'):
        line = 'dot' + line[1:]

    # Initialize variables for processing
    count_at_sign = 0
    transformed_list = []
    
    # If the first character is "@", prepend "at" to the string
    if line.startswith('@'):
        line = 'at' + line[1:]

    # Iterate through each character in the transformed line
    for character in line:
        if character == '@':
            if count_at_sign > 0:
                # Replace with "at" to prevent consecutive "at"
                transformed_list.append("at")
                count_at_sign = 1
            else:
                # First occurrence of "@"
                transformed_list.append("@")
                count_at_sign = 1
        else:
            # Append the current character as is
            transformed_list.append(character)

    # Join the transformed list into a single string
    final_string = ''.join(transformed_list)

    # If the last character is ".", replace it with "dot"
    if final_string.endswith('.'):
        final_string = final_string[:-1] + "dot"

    # Output the final transformed string
    print(final_string)
