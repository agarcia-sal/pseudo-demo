# Function to transform the input string according to specified rules
def transform_input_string():
    # Read input from user and remove unnecessary whitespace
    input_string = input().strip()

    # Replace occurrences of "dot" with "." and "at" with "@" in the input string
    input_string = input_string.replace("dot", ".")
    input_string = input_string.replace("at", "@")

    # Check if the input starts with a dot and modify accordingly
    if input_string.startswith("."):
        input_string = "dot" + input_string[1:]

    # Initialize a counter and an empty list for constructing the output
    counter = 0
    character_list = []

    # Check if the input starts with an @ and modify accordingly
    if input_string.startswith("@"):
        input_string = "at" + input_string[1:]

    # Iterate through each character in the input string
    for character in input_string:
        # Check for the occurrence of '@' character
        if character == "@":
            if counter > 0:
                # Append "at" to character_list if we already encountered an '@'
                character_list.append("at")
                counter = 1 
            else:
                # Append "@" to character_list for the first occurrence
                character_list.append("@")
                counter = 1
        else:
            # If the character is not '@', simply add it to character_list
            character_list.append(character)

    # Join all characters in character_list into a single string
    output_string = ''.join(character_list)

    # Check if the final character is a dot and modify accordingly
    if output_string.endswith("."):
        output_string = output_string[:-1] + "dot"

    # Print the final output
    print(output_string)

# Example test cases (uncomment to test)
# Test case 1: "dot.example@domain.at"
# Expected output: "dot.example@domain.at"
# Test case 2: ".example@domain.at"
# Expected output: "dot.example@domain.at"
# Test case 3: "example.com"
# Expected output: "example.com"
# Test case 4: "@example.com"
# Expected output: "atexample.com"
# Test case 5: "example.com."
# Expected output: "example.dot"

transform_input_string()
