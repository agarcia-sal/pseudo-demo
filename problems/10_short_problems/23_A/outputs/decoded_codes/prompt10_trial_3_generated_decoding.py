def read_input_line():
    return input().strip()  # Read a line of input and remove any trailing newlines

def extract_substring(s, start_index, length):
    return s[start_index:start_index + length]

def find_substring(s, substring, start_index):
    return substring in s[start_index:]

def main():
    input_line = read_input_line()  # Read input line
    n = len(input_line)  # Get the length of the input line
    result_value = 0  # Initialize a variable to store the result

    # Loop over all possible lengths for substrings
    for length in range(1, n):  # Start from 1 because length 0 is trivial
        # Loop over each starting position for substrings of the given length
        for start_index in range(n - length + 1):  # Ensure we don't go out of bounds
            # Extract substring from startIndex with the specified length
            substring = extract_substring(input_line, start_index, length)

            # Check if the substring can be found in the remaining part of the string
            if find_substring(input_line, substring, start_index + 1):
                result_value = length  # Update resultValue with the current length
                break  # Exit the inner loop if a match is found

    # Output the result
    print(result_value)  # Display the final result

if __name__ == "__main__":
    main()
