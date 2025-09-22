def transform_email_input():
    # Step 1: Read Input
    email_input = input().strip()  # Obtain user input and remove whitespace

    # Step 2: Replace Substrings
    email_input = email_input.replace("dot", ".")
    email_input = email_input.replace("at", "@")

    # Step 3: Ensure Starting Character Rule
    if email_input.startswith('.'):
        email_input = 'dot' + email_input  # Prepend 'dot' if the string starts with '.'

    # Step 4: Initialize State Variables
    previous_at_count = 0
    output_characters = []  # List to hold processed characters

    # Step 5: Handle the '@' Character
    if email_input.startswith('@'):
        email_input = 'at' + email_input[1:]  # Change the first char to 'at'

    # Step 6: Process Each Character in the String
    for current_character in email_input:
        if current_character == '@':
            if previous_at_count > 0:
                output_characters.append("at")  # Append "at" if we've seen '@' before
            else:
                output_characters.append(current_character)  # Append '@'
            previous_at_count = 1  # Set previous 'at' count to 1
        else:
            output_characters.append(current_character)  # Append any other character

    # Step 7: Form the Final Output String
    final_output = ''.join(output_characters)  # Join to create a single string
    if final_output.endswith('.'):
        final_output = final_output[:-1] + "dot"  # Replace last '.' with 'dot'

    # Step 8: Display the Result
    print(final_output)

# Expected usage
transform_email_input()
