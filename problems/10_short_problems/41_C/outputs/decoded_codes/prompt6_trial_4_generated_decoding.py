def process_input():
    # Read input from the user and remove leading/trailing whitespace
    input_string = input().strip()
    
    # Replace specific words with their corresponding symbols
    input_string = input_string.replace("dot", ".").replace("at", "@")

    # If the first character is a '.', prepend 'dot' to the string
    if input_string and input_string[0] == '.':
        input_string = "dot" + input_string[1:]

    # Initialize counter and list for building output
    count_at = 0
    output_list = []

    # If the first character is an '@', prepend 'at' to the string
    if input_string and input_string[0] == '@':
        input_string = "at" + input_string[1:]

    # Iterate through each character in the modified input_string
    for character in input_string:
        if character == '@':
            # If we have already processed an '@', append "at"
            if count_at > 0:
                output_list.append("at")
                count_at = 1
            else:
                output_list.append("@")
                count_at = 1
        else:
            # If the character is not '@', just append it to the output_list
            output_list.append(character)

    # Join the output_list into a single string
    output_string = ''.join(output_list)

    # Replace a trailing '.' with 'dot' if it exists
    if output_string and output_string[-1] == '.':
        output_string = output_string[:-1] + "dot"

    # Print the final processed output
    print(output_string)

# You can call the function to test its functionality
process_input()
