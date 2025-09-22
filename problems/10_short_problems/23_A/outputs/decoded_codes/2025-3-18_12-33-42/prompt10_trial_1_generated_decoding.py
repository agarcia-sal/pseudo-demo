def find_longest_repeated_substring():
    # Step 1: Read input line
    line = input().rstrip()  # Removing the last character (newline)

    # Step 2: Initialize variables
    n = len(line)
    rv = 0  # Result variable to store the length of the longest repeated substring

    # Step 3: Loop through possible substring lengths (from 0 to n-1)
    for l in range(n):
        # Step 4: Nested loop to check all starting positions for substrings
        for i in range(n):
            substring = line[i:i + l]  # Extracting the substring of length l
            # Step 5: Check if there is a repeated substring
            if substring in line[i + 1:]:
                rv = l  # Update the value of rv to the current length l
                break  # Exit the inner loop since we found a repeat
        else:
            continue  # Continue outer loop if no break occurred
        break  # Exit outer loop if inner loop was broken

    # Step 6: Output the result
    print(rv)

# To run the function, you can simply call:
find_longest_repeated_substring()
