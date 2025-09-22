def main():
    # Read a line of input from the user and remove the last character (newline)
    line = input().strip()

    # Determine the length of the input line
    n = len(line)
    rv = 0  # Initialize the result variable

    # Loop through all possible lengths of substrings from 0 to n-1
    for l in range(n):
        # Loop through the starting index of the substring
        for i in range(n):
            # Check if the substring from index i to i+l exists later in the string
            substring = line[i:i+l+1]
            if line.find(substring, i + 1) != -1:  # +1 to search after the current position
                rv = l  # Update result variable with current length l
                break  # Exit the inner loop
        else: 
            continue  # This else is associated with the inner for, only runs if not broken
        break  # Break the outer loop if inner loop was exited due to a match

    # Print the result variable indicating the length of the substring found
    print(rv)

if __name__ == "__main__":
    main()
