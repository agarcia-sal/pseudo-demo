def process_input():
    # Step 1: Read Input and clean whitespace
    input_line = input().strip()

    # Step 2: Replace substrings "dot" with "." and "at" with "@"
    input_line = input_line.replace("dot", ".").replace("at", "@")

    # Step 3: Check for leading dot
    if input_line.startswith("."):
        input_line = "dot" + input_line[1:]

    # Initialize tracking variables
    counter = 0
    characters_list = []
    
    # Step 5: Check for leading at
    if input_line.startswith("@"):
        input_line = "at" + input_line[1:]

    # Step 6: Iterate through each character
    for current_char in input_line:
        if current_char == "@":
            if counter > 0:
                characters_list.append("at")
                counter = 1
            else:
                characters_list.append("@")
                counter = 1
        else:
            characters_list.append(current_char)
            counter = 0

    # Step 7: Join characters
    joined_characters = ''.join(characters_list)

    # Step 8: Check for trailing dot
    if joined_characters.endswith("."):
        joined_characters = joined_characters[:-1] + "dot"

    # Step 9: Display the result
    print(joined_characters)

# Call the function to execute
process_input()
