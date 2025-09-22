def main():
    # Step 1: Read input and initialize variables
    input_string = input().strip()  # Read input and remove trailing spaces
    index = 0  # Start index
    answer = ""  # Initialize answer as an empty string

    # Step 2: Process each character in the input string
    while index < len(input_string):
        if input_string[index] == '.':
            answer += '0'  # Append '0' for single dot
            index += 1  # Move to the next character
        elif index + 1 < len(input_string) and input_string[index + 1] == '.':
            answer += '1'  # Append '1' for two consecutive dots
            index += 2  # Move past both dots
        else:
            answer += '2'  # Append '2' for any other character
            index += 2  # Move to the next character after the current one

    # Step 3: Output the result
    print(answer)

if __name__ == "__main__":
    main()
