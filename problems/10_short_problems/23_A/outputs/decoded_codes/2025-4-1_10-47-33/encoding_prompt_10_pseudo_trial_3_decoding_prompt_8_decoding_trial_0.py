def trim_last_character(s):
    return s[:-1]

def find_substring(line, substring, start_index):
    return line.find(substring, start_index)

def main():
    # Step 1: Read a line of input from the standard input
    line = input()
    
    # Step 2: Remove the last character from the input line (typically a newline)
    line = trim_last_character(line)

    # Step 3: Determine the length of the line
    n = len(line)

    # Step 4: Initialize a variable to store the result
    rv = 0

    # Step 5: Iterate through possible substring lengths from 0 to n-1
    for l in range(n):
        # Step 6: Iterate through each character in the line
        for i in range(n):
            # Step 7: Check if a substring of length l starting at index i
            #         can be found elsewhere in the line after index i
            if find_substring(line, line[i:i+l], i + 1) != -1:
                # Step 8: Update rv to the current length l
                rv = l
                # Step 9: Exit the inner loop since a match is found
                break

    # Step 10: Output the result
    print(rv)

# To execute the main function
if __name__ == '__main__':
    main()
