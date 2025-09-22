def read_input():
    # Reads a line of input from standard input and strips the newline
    return input().strip()

def find_substring(main_string, substring, start):
    # Searches for substring in main_string starting from 'start' index
    return main_string.find(substring, start)

def longest_prefix_length(input_string):
    string_length = len(input_string)
    longest_prefix_length = 0

    # Loop through potential prefix lengths
    for current_length in range(1, string_length):  # Start from 1 to skip empty prefix
        prefix = input_string[:current_length]  # Get the current prefix
        
        # Check every starting position in the string
        for start_position in range(string_length):
            # Check if the prefix exists again after the start_position
            if find_substring(input_string, prefix, start_position + 1) != -1:
                longest_prefix_length = current_length  # Update length if a match is found
                break  # Exit the start_position loop if a match is found

    return longest_prefix_length

def main():
    input_string = read_input()  # Get input from the user
    result = longest_prefix_length(input_string)  # Compute longest prefix length
    print(result)  # Output the result

if __name__ == "__main__":
    main()
