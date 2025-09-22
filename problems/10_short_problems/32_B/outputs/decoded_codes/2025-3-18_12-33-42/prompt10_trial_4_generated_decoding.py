def main():
    # Read input and remove any leading/trailing whitespace
    input_string = input().strip()
    index = 0
    result = ""

    # Loop through the characters in the input string
    while index < len(input_string):
        # Check the current character in the input string
        if input_string[index] == '.':
            result += '0'   # Append '0' to result
            index += 1      # Move to the next character
        elif index + 1 < len(input_string) and input_string[index + 1] == '.':
            result += '1'   # Append '1' to result
            index += 2      # Skip the next character
        else:
            result += '2'   # Append '2' to result
            index += 2      # Skip the next character

    # Output the final result
    print(result)

# Run the main function
if __name__ == "__main__":
    main()
