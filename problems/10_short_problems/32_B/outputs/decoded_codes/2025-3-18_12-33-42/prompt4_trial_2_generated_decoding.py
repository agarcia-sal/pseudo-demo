def main():
    # Read input string from standard input
    input_string = input()
    trimmed_string = input_string.strip()  # Trim whitespace from the input

    # Initialize index and result string
    index = 0
    result = ""

    # Loop through the characters in the trimmed input string
    while index < len(trimmed_string):
        if trimmed_string[index] == '.':
            # Add '0' to the result for a single dot
            result += '0'
            index += 1
        elif index + 1 < len(trimmed_string) and trimmed_string[index + 1] == '.':
            # Add '1' to the result for a 'dots' (two consecutive dots) pattern
            result += '1'
            index += 2
        else:
            # Default case for replacement when neither condition is met
            result += '2'
            index += 2

    # Output the final transformed result
    print(result)

if __name__ == "__main__":
    main()
