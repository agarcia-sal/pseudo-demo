def convert_dots_to_digits():
    # Step 2: Read Input
    input_string = input().strip()  # Read input and remove excess whitespace

    # Step 3: Initialize Variables
    index = 0
    result = ""  # To store the output

    # Step 4: Process the Input String
    while index < len(input_string):
        if input_string[index] == '.':
            result += '0'  # Append '0' for a single dot
            index += 1  # Move to the next character
        elif index + 1 < len(input_string) and input_string[index + 1] == '.':
            result += '1'  # Append '1' for two consecutive dots
            index += 2  # Skip the next character as well
        else:
            result += '2'  # Append '2' for any other character
            index += 2  # Skip the next character

    # Step 5: Output the Result
    print(result)

# Uncomment the line below to run the function if testing the code separately
# convert_dots_to_digits()
