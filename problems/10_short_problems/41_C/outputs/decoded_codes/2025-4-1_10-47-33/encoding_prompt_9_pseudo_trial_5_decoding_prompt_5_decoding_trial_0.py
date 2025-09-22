# Function to transform a specific input string based on keyword substitutions and formatting
def transform_input_string():
    # Step 1: Receive Input
    user_input = input().strip()  # Read and trim the user input
    
    # Step 2: Replace Keywords
    modified_string = user_input.replace("dot", ".").replace("at", "@")  # Replace 'dot' with '.' and 'at' with '@'
    
    # Step 3: Check for Leading Symbols
    if modified_string and modified_string[0] == ".":
        modified_string = "dot" + modified_string  # Prepend 'dot' if the first character is '.'
    
    # Step 4: Initialize Variables
    at_counter = 0  # Counter for occurrences of "@"
    characters = []  # List to hold characters
    length = 0  # Variable to store the length (not used directly in logic)
    
    # Step 5: Check for Leading "at"
    if modified_string and modified_string[0] == "@":
        modified_string = "at" + modified_string  # Prepend 'at' if the first character is '@'
    
    # Step 6: Process Each Character
    for char in modified_string:  # Iterate through each character in the string
        if char == "@":
            if at_counter > 0:
                characters.append("at")  # Append 'at' if another '@' has been encountered
                at_counter = 1  # Set counter to 1 indicating '@' has been found
            else:
                characters.append("@")  # Append '@' to the list
                at_counter = 1  # Increment the counter
        else:
            characters.append(char)  # Append the character directly to the list
    
    # Step 7: Join Characters
    final_string = ''.join(characters)  # Join all characters into a single string
    
    # Step 8: Check Trailing Symbols
    if final_string and final_string[-1] == ".":
        final_string = final_string[:-1] + "dot"  # Replace the trailing '.' with 'dot'
    
    # Step 9: Output the Result
    print(final_string)  # Print the final transformed string

# Example test cases can be constructed but will not be included as per instructions.
# transform_input_string()  # Uncomment to run the function and test
