def process_email_input():
    # Step 1: Read input and strip whitespace
    email_input = input().strip()

    # Step 2: Replace 'dot' with '.' and 'at' with '@'
    email_input = email_input.replace("dot", ".").replace("at", "@")

    # Step 3: Ensure starting character rule
    if email_input.startswith('.'):
        email_input = 'dot' + email_input  # Prepend 'dot' to maintain valid format

    # Step 4: Initialize state variables
    previous_at_count = 0
    output_characters = []

    # Step 5: Handle the first '@' character
    if email_input.startswith('@'):
        email_input = 'at' + email_input[1:]  # Replace first character with 'at'

    # Step 6: Process each character in the string
    for current_character in email_input:
        if current_character == '@':
            if previous_at_count > 0:
                output_characters.append("at")  # Appending 'at' again if multiple '@'
                previous_at_count = 1  # Reset count since we appended
            else:
                output_characters.append('@')  # First '@' occurrence
                previous_at_count = 1  # Increment to indicate we have seen '@'
        else:
            output_characters.append(current_character)  # Append current character if not '@'

    # Step 7: Form the final output string
    final_output = ''.join(output_characters)
    if final_output.endswith('.'):
        final_output = final_output[:-1] + "dot"  # Replace last '.' with 'dot'

    # Step 8: Display the final result
    print(final_output)

# Run the function to process email input
process_email_input()
