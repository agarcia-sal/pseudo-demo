# Function to process the email string and replace keywords with symbols
def process_email_string():
    # Step 1: Receive input and strip any leading/trailing spaces
    email_input = input().strip()

    # Step 2: Replace "dot" with "." and "at" with "@"
    email_modified = email_input.replace("dot", ".").replace("at", "@")

    # Step 3: Check leading character for "."
    if email_modified.startswith("."):
        email_modified = "dot" + email_modified[1:]

    # Step 4: Initialize counter and list for processed characters
    counter = 0
    processed_chars = []

    # Step 5: Check if the modified string starts with "@"
    if email_modified.startswith("@"):
        processed_chars.append("at")
        processed_chars.append(email_modified[1:])
        counter = 1
    else:
        # Step 6: Process each character in the modified string
        for character in email_modified:
            if character == "@":
                if counter > 0:
                    processed_chars.append("at")
                    counter += 1
                else:
                    processed_chars.append(character)
                    counter += 1
            else:
                processed_chars.append(character)

    # Step 7: Reconstruct the string
    email_reconstructed = ''.join(processed_chars)

    # Step 8: Check for trailing "." and replace it with "dot"
    if email_reconstructed.endswith("."):
        email_reconstructed = email_reconstructed[:-1] + "dot"

    # Step 9: Output the final processed string
    print(email_reconstructed)

# Sample test cases (commented) to consider for testing the function
# Input: "john.doe@example.com" -> Output: "john.doe@example.com"
# Input: "john dot doe at example dot com" -> Output: "john.doe@example.com"
# Input: "dotjohn doe at example com" -> Output: "dotjohn.doe@example.com"
# Input: "john doe at example.com dot" -> Output: "john.doe@example.com"
