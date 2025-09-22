def find_longest_repeated_substring():
    # Step 1: Read input and initialize variables
    line = input().strip()  # Read a line of input and strip any newline characters
    n = len(line)  # Get the length of the input string
    result = 0  # This variable stores the length of the longest repeated substring

    # Step 2: Iterate through possible substring lengths l from 0 to n-1
    for l in range(n):  # l varies from 0 to n-1
        # Step 3: Check for substring presence
        for i in range(n):  # Check each starting index i
            substring = line[i:i+l]  # Extract substring from index i of length l
            
            # Step 4: Check if this substring exists later in the string
            if substring and line.find(substring, i + 1) != -1:
                result = l  # Update result with the current length l
                break  # Exit the inner loop as the substring is found

    # Step 5: Output the result
    print(result)  # Display the final value of result

# Call the function to execute
find_longest_repeated_substring()
