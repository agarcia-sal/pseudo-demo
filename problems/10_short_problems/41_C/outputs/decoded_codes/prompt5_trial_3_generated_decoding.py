# Function to process an email address string
def process_email_string():
    # Step 1: Read input and trim whitespace
    email_input = input().strip()
    
    # Step 2: Replace keywords with appropriate characters
    email_input = email_input.replace("dot", ".").replace("at", "@")
    
    # Step 3: Adjust starting character if it starts with a "."
    if email_input.startswith("."):
        email_input = "dot" + email_input
    
    # Step 4: Initialize variables
    at_counter = 0
    result_list = []

    # Step 5: Handle starting "at" character
    if email_input.startswith("@"):
        email_input = "at" + email_input[1:]

    # Step 6: Process each character in the modified string
    for char in email_input:
        if char == "@":
            if at_counter > 0:
                result_list.append("at")
                at_counter = 1
            else:
                result_list.append("@")
                at_counter = 1
        else:
            result_list.append(char)

    # Step 7: Join result characters into final string
    final_string = ''.join(result_list)

    # Step 8: Adjust ending character if it ends with "."
    if final_string.endswith("."):
        final_string = final_string[:-1] + "dot"

    # Step 9: Output the result
    print(final_string)

# Call the function to execute the process
process_email_string()
