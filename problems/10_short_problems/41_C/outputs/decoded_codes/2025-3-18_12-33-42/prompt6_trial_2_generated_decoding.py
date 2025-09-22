# Step 1: Read Input
user_input = input().strip()  # Read input and remove leading/trailing whitespace

# Step 2: Replace Identifiers
user_input = user_input.replace("dot", ".").replace("at", "@")

# Step 3: Ensure Proper Formatting
if user_input.startswith('.'):
    user_input = "dot" + user_input[1:]  # Prepend "dot" if the first character is a period

# Step 4: Initialize Variables
counter = 0  # Initialize counter variable
formatted_characters = []  # Create an empty list to store the formatted characters

# Step 5: Check for Initial '@' Character
if user_input.startswith('@'):
    user_input = "at" + user_input[1:]  # Prepend "at" if the first character is "@"

# Step 6: Process Each Character
for char in user_input:
    if char == "@":
        if counter > 0:  # If counter is greater than 0, means we already have an '@'
            formatted_characters.append("at")  # Append "at" instead of another "@"
            counter = 1  # Reset counter to count new "@" occurrence
        else:
            formatted_characters.append("@")  # Append "@" for the first occurrence
            counter = 1  # Set counter to 1
    else:
        formatted_characters.append(char)  # Append the character to the list

# Step 7: Create Final String
final_output = ''.join(formatted_characters)  # Join the characters list into a single string

# Step 8: Handle Trailing Period
if final_output.endswith('.'):
    final_output = final_output[:-1] + "dot"  # Remove the period and append "dot"

# Step 9: Output the Result
print(final_output)  # Print the final formatted output
