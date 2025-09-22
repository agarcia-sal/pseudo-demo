def main():
    # Read input
    line = input().rstrip()  # Read input and remove the newline character
    n = len(line)  # Get the length of the line
    rv = 0  # Initialize return value

    # Outer loop for substring lengths
    for l in range(n):  # l goes from 0 to n-1
        # Inner loop for checking substrings
        for i in range(n):  # i goes from 0 to n-1
            # Check if the substring exists in the remainder of the string
            substring = line[i:i+l]  # Get the substring of length l starting at index i
            
            # Ensure we're not checking empty substrings or beyond the string's bounds
            if substring and line.find(substring, i + 1) != -1:
                rv = l  # Update rv with the current length
                break  # Exit inner loop if a valid substring is found

    # Output the result
    print(rv)

# Run the main function
if __name__ == "__main__":
    main()
