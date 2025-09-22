def find_longest_substring():
    # Step 1: Read input and initialize variables
    line = input()  # Read a line of input from standard input
    line = line[:-1]  # Remove the last character from the line
    n = len(line)  # Get the length of the line
    rv = 0  # This variable stores the result

    # Step 2: Iterate through lengths l from 0 to n-1
    for l in range(n):  # l ranges from 0 to n-1
        # Step 3: Check for substring presence
        for i in range(n):  # i ranges from 0 to n-1
            # Step 4: Check if the substring exists later in the string
            substring = line[i:i+l]  # Extract the substring
            if substring and line.find(substring, i + 1) != -1:  # Check if substring exists from index i+1
                rv = l  # Update rv with the current length l
                break  # Exit the inner loop as the substring is found

    # Step 5: Output the result
    print(rv)  # Display the final value of rv

# To run the function
find_longest_substring()
