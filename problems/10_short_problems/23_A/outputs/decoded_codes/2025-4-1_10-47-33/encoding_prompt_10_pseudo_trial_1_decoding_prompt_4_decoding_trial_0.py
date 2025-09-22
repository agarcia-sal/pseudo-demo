# Begin the function to process input and calculate the result
def find_longest_repeated_substring():
    # Step 1: Read input and initialize variables
    line = input().strip()  # Read a line of input and strip any trailing newline characters
    n = len(line)  # Determine the length of the input line
    rv = 0  # This variable will store the result - the size of the longest repeating substring

    # Step 2: Iterate through lengths l from 0 to n-1
    for l in range(n):  # l ranges from 0 to n-1
        # Step 3: Check for substring presence
        for i in range(n):  # i ranges through each character index in the string
            # Step 4: Check if the substring exists later in the string
            # We extract the substring line[i:i+l] and check its presence from index i+1 onward
            if line[i:i+l] in line[i+1:]:
                rv = l  # Update rv with the current length l
                break  # Exit the inner loop as we found a repeating substring
        else:
            # If we didn't break out of the inner loop, no matching substring was found for this length
            continue  # Continue to the next length

    # Step 5: Output the result
    print(rv)  # Print the final value of rv

# Call the function to execute
find_longest_repeated_substring()
