def read_input():
    # Reading input from standard input
    return input().strip()

def replace_all(string, old, new):
    # Replace all occurrences of old substring with new substring
    return string.replace(old, new)

def main():
    # Step 1: Read input and trim leading/trailing spaces
    input_string = read_input()

    # Step 2: Replace 'dot' with '.' and 'at' with '@'
    transformed_string = replace_all(input_string, 'dot', '.')
    transformed_string = replace_all(transformed_string, 'at', '@')

    # Step 3: Prepend 'dot' if the transformed string starts with '.'
    if transformed_string.startswith('.'):
        transformed_string = 'dot' + transformed_string[1:]

    # Step 4: Initialize a counter and a list to hold characters
    counter = 0
    character_list = []

    # Step 5: Prepend 'at' if the string starts with '@'
    if transformed_string.startswith('@'):
        transformed_string = 'at' + transformed_string[1:]

    # Step 6: Iterate through each character in the transformed string
    for character in transformed_string:
        if character == '@':
            # Replace second and subsequent '@' with 'at'
            if counter > 0:
                character_list.append('at')
                counter = 1
            else:
                character_list.append('@')
                counter += 1
        else:
            # Add non-special characters to the list
            character_list.append(character)

    # Step 7: Join the characters in the list to form the final string
    final_string = ''.join(character_list)

    # Step 8: Replace the last character '.' with 'dot' if necessary
    if final_string.endswith('.'):
        final_string = final_string[:-1] + 'dot'

    # Step 9: Print the final transformed string
    print(final_string)

if __name__ == "__main__":
    main()
