# Function to process the input string according to specified rules
def process_string():
    # Read input from the user and trim whitespace
    input_string = input().strip()
    
    # Replace specific words with symbols
    input_string = input_string.replace("dot", ".")
    input_string = input_string.replace("at", "@")
    
    # Check if the first character is a period and adjust if necessary
    if input_string.startswith("."):
        input_string = "dot" + input_string[1:]  # Prepend "dot"
    
    # Initialize counter for "at" occurrences
    at_counter = 0
    list_of_characters = []  # List to store characters

    # Check if the first character is "@" and adjust if necessary
    if input_string.startswith("@"):
        input_string = "at" + input_string[1:]  # Prepend "at"
    
    # Iterate over each character in the string
    for character in input_string:
        if character == "@":
            if at_counter > 0:
                list_of_characters.append("at")  # Append "at" if counter > 0
                at_counter = 1  # Reset counter
            else:
                list_of_characters.append("@")  # Append "@" first occurrence
                at_counter = 1
        else:
            list_of_characters.append(character)  # Append the character

    # Join the characters in the list to form the output string
    final_output_string = ''.join(list_of_characters)
    
    # Check if the last character is a period and adjust if necessary
    if final_output_string.endswith("."):
        final_output_string = final_output_string[:-1] + "dot"  # Replace last "." with "dot"
    
    # Print the final output
    print(final_output_string)

# Call the function to execute the processing
process_string()
