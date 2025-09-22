def main():
    # Read input line from standard input and remove the trailing newline character.
    line = input().strip()
    
    # Set variable 'n' to the length of the input line.
    n = len(line)
    
    # Initialize variable 'rv' to 0. This will hold the result.
    rv = 0

    # Iterate over each length 'l' from 0 to n-1 (inclusive).
    for l in range(n):
        # For each index 'i' from 0 to n-1 (inclusive).
        for i in range(n):
            # Extract the substring from 'line', starting at index 'i' with length 'l'.
            substring = line[i:i + l]
            
            # Check if this substring appears again in 'line' starting from index 'i + 1'.
            if substring in line[i + 1:]:
                # If the substring is found, update 'rv' to the current value of 'l'.
                rv = l
                # Break out of the inner loop since we found a match.
                break
    
    # Print the value of 'rv'. This is the final result.
    print(rv)

# Execute the main function
if __name__ == "__main__":
    main()
