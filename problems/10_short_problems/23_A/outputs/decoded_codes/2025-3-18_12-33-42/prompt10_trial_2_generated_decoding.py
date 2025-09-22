def main():
    # Read a line of input and remove the trailing newline character
    input_line = input().strip()
    n = len(input_line)
    reverse_value = 0

    # Loop through possible lengths for substrings
    for length in range(n):  # from 0 to n - 1
        # Loop to check each starting position for the substring
        for start_index in range(n):  # from 0 to n - 1
            # Extract the substring from the current start index and of the current length
            substring = input_line[start_index:(start_index + length)]

            # Check if the substring appears later in the line
            if input_line.find(substring, start_index + 1) != -1:
                # Update the reverse_value if a match is found
                reverse_value = length
                break  # Exit the inner loop if a match is found

    # Output the reverse_value
    print(reverse_value)

if __name__ == "__main__":
    main()
