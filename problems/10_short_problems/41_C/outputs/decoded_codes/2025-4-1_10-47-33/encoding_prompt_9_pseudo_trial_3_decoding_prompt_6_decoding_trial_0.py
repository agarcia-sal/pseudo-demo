# Step 1: Receive Input
email_input = input().strip()  # Read input and remove surrounding whitespace

# Step 2: Replace Text Patterns
email_input = email_input.replace("dot", ".")  # Replace 'dot' with '.'
email_input = email_input.replace("at", "@")    # Replace 'at' with '@'

# Step 3: Adjust Leading Character
if email_input.startswith("."):  # Check if the string starts with '.'
    email_input = "dot" + email_input  # Prepend 'dot'

# Step 4: Initialize Variables
at_counter = 0  # Counter for occurrences of '@'
char_list = []  # Empty list to store characters

# Step 5: Check for Leading "at"
if email_input.startswith("@"):  # If the string starts with '@'
    email_input = "at" + email_input  # Prepend 'at' to the string

# Step 6: Iterate Through Each Character
for char in email_input:
    if char == "@":  # Check if the character is '@'
        if at_counter > 0:  # If we've already seen an '@'
            char_list.append("at")  # Append 'at' to the list
            at_counter = 1  # Reset counter to 1
        else:
            char_list.append("@")  # Append '@' to the list
            at_counter = 1  # Increment counter
    else:
        char_list.append(char)  # Append the character to the list

# Step 7: Reconstruct the String
final_email = ''.join(char_list)  # Join the list of characters

# Step 8: Adjust Trailing Character
if final_email.endswith("."):  # If the string ends with '.'
    final_email = final_email[:-1] + "dot"  # Replace last '.' with 'dot'

# Step 9: Output the Result
print(final_email)  # Print the final transformed string
