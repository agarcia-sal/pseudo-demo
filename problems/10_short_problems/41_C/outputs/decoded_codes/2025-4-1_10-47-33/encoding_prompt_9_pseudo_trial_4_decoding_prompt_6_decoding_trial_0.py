# Step 1: Receive input and remove leading/trailing spaces
email_input = input().strip()

# Step 2: Replace keywords
email_input = email_input.replace("dot", ".").replace("at", "@")

# Step 3: Check and handle leading character
if email_input.startswith("."):
    email_input = "dot" + email_input[1:]

# Step 4: Initialize the list and counter
at_counter = 0
processed_email = []

# Step 5: Check for leading "at"
if email_input.startswith("@"):
    processed_email.append("at")
    processed_email.append(email_input[1:])
else:
    processed_email.append(email_input)

# Step 6: Process each character in the modified string
for char in email_input:
    if char == "@":
        if at_counter > 0:
            processed_email.append("at")
            at_counter = 1  # reset counter, prevent multiple "at"
        else:
            processed_email.append("@")
            at_counter = 1
    else:
        processed_email.append(char)

# Step 7: Reconstruct the string
final_email = ''.join(processed_email)

# Step 8: Check for trailing character and replace if needed
if final_email.endswith("."):
    final_email = final_email[:-1] + "dot"

# Step 9: Output the result
print(final_email)
