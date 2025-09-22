def main():
    # Step 1: Read input, omitting the last character
    line = input()[:-1]

    # Step 2: Determine the length of the input string
    n = len(line)
    rv = 0  # This will hold the maximum length of substring found

    # Step 3: Loop to check for repeated substrings
    for l in range(n):  # l goes from 0 to n - 1
        for i in range(n):  # i goes from 0 to n - 1
            # Check if the substring line[i:i+l] appears again in line
            if line[i:i + l] in line[i + 1:]:
                rv = l  # Update rv with the current length l
                break  # Exit the inner loop as we found a match

    # Step 4: Output the result
    print(rv)

# Run the main function
if __name__ == "__main__":
    main()
