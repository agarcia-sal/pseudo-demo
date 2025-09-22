def read_line_from_input():
    return input()

def get_length_of(string):
    return len(string)

def extract_substring(string, start_index, length):
    return string[start_index:start_index + length]

def is_substring_found(string, substring, start_index):
    return substring in string[start_index:]

def main():
    input_line = read_line_from_input().rstrip()
    length_of_line = get_length_of(input_line)
    result_value = 0

    # Loop through all possible lengths of substrings
    for substring_length in range(length_of_line):
        # Check each starting index for the substring of the current length
        for start_index in range(length_of_line):
            # Extract the substring for the current startIndex and substringLength
            current_substring = extract_substring(input_line, start_index, substring_length)

            # Check if the currentSubstring exists in inputLine starting from the next position
            if is_substring_found(input_line, current_substring, start_index + 1):
                # Update resultValue with the current substring length
                result_value = substring_length
                # Break out of the inner loop since a match was found
                break

    print(result_value)

if __name__ == "__main__":
    main()
