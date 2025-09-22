def main():
    # Read a line of input from standard input
    input_line = input().rstrip()  # Remove the trailing newline character
    string_length = len(input_line)
    result_value = 0

    # Loop for each length l from 0 to string_length - 1
    for length in range(string_length):
        # Loop for each starting index i from 0 to string_length - 1
        for index in range(string_length):
            # Ensure we're not out of bounds when extracting a substring
            if index + length <= string_length:
                # Extract a substring from input_line with length l starting at index i
                substring = input_line[index:index + length]
                
                # Check if this substring exists in inputLine after index i
                if substring in input_line[index + 1:]:
                    # Update result_value to the current length l
                    result_value = length
                    # Exit the inner loop
                    break
            
    # Output the final result_value
    print(result_value)

if __name__ == "__main__":
    main()
