def process_input():
    # Read user input and remove leading/trailing whitespace
    input_string = input().strip()

    # Replace "dot" with "." and "at" with "@" in the input string
    input_string = input_string.replace("dot", ".").replace("at", "@")

    # Check if the input starts with a dot to prepend "dot"
    if input_string.startswith('.'):
        input_string = "dot" + input_string[1:]

    # Initialize a counter and an empty list for building output
    counter = 0
    output_list = []

    # Check for a starting '@' and adjust accordingly
    if input_string.startswith('@'):
        output_list.append("at")
        input_string = input_string[1:]

    # Iterate through each character in the modified input_string
    for char in input_string:
        if char == '@':
            # Append "at" for each subsequent '@'
            if counter > 0:
                output_list.append("at")
            else:
                output_list.append("@")
            counter += 1
        else:
            output_list.append(char)

    # Join the output_list into a single string
    final_string = ''.join(output_list)

    # If the final string ends with a dot, replace it with "dot"
    if final_string.endswith('.'):
        final_string = final_string[:-1] + "dot"

    # Output the final processed string
    print(final_string)

# Call the function to execute the process
process_input()
