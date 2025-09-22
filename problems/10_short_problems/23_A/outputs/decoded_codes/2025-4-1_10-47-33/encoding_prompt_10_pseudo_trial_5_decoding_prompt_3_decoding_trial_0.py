# Step 1: Import standard input functionality is implied by using input()

def find_longest_repeated_substring():
    # Step 2: Read a line of input from standard input and remove the trailing newline character.
    line = input().strip()
    n = len(line)  # Step 3: Set variable 'n' to the length of the input line.
    rv = 0  # Step 4: Initialize variable 'rv' to 0. This will hold the result.

    # Step 5: FOR each length 'l' from 0 to n-1 DO:
    for l in range(n):
        # Step 6: FOR each index 'i' from 0 to n-1 DO:
        for i in range(n):
            # Step 7: Extract the substring from 'line' starting at index 'i' with length 'l'.
            substring = line[i:i+l]
            # Check if the substring appears again in 'line' starting from index 'i + 1'.
            if substring in line[i + 1:]:
                # Step 9: IF the substring is found THEN:
                rv = l  # Step 10: Set 'rv' to the value of 'l'.
                break  # Step 11: Break out of the inner loop.

    # Step 12: Print the value of 'rv'. Output the result.
    print(rv)

# Call the function to execute the code
find_longest_repeated_substring()
