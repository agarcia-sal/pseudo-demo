# Function to convert specific text input into a standard email format
def convert_to_email_format():
    # Step 1: Read Input
    user_input = input().strip()  # Remove leading and trailing whitespace
    
    # Step 2: Replace Keywords
    modified_string = user_input.replace("dot", ".").replace("at", "@")
    
    # Step 3: Check for Leading Dot
    if modified_string.startswith("."):
        modified_string = "dot" + modified_string  # Prepend "dot" if leading dot exists
    
    # Step 4: Initialize Variables
    co = 0  # Counter for occurrences of "@"
    c = []  # List to store processed characters

    # Step 5: Fix the Leading At
    if modified_string.startswith("@"):
        modified_string = "at" + modified_string  # Prepend "at" if leading @ exists
    
    # Step 6: Process Each Character
    for char in modified_string:
        if char == "@":
            if co > 0:
                c.append("at")  # Add "at" if already seen an "@" before
                co = 1  # Reset count
            else:
                c.append("@")  # First "@" encountered
                co = 1  # Increment counter
        else:
            c.append(char)  # Append normal characters
    
    # Step 7: Combine Characters
    combined_string = ''.join(c)  # Join list into a single string

    # Step 8: Adjust Trailing Dot
    if combined_string.endswith("."):
        combined_string = combined_string[:-1] + "dot"  # Replace trailing dot with "dot"
    
    # Step 9: Output the Result
    print(combined_string)  # Print final modified string

# Example Usage
convert_to_email_format()
