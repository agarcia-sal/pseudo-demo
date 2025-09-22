def translate_dots_to_numbers():
    # Step 1: Read Input
    input_string = input().strip()  # Removing extra spaces around input

    # Step 2: Initialize Variables
    index = 0
    output_string = ""

    # Step 3: Process Input Until End
    while index < len(input_string):
        # Check if current character is a dot
        if input_string[index] == '.':
            output_string += '0'
            index += 1  # Move to next character
        # Check if the next character is a dot
        elif index + 1 < len(input_string) and input_string[index + 1] == '.':
            output_string += '1'
            index += 2  # Skip to character after next
        else:
            output_string += '2'
            index += 2  # Skip to character after next

    # Step 4: Output Result
    print(output_string)

# Example usage
if __name__ == "__main__":
    translate_dots_to_numbers()
