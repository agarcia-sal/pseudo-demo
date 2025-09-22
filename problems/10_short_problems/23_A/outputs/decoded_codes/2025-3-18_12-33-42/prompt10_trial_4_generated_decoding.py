def find_longest_repeated_substring():
    # Step 1: Read input and remove trailing newline
    input_line = input().rstrip()
    
    # Step 2: Determine the length of the input
    n = len(input_line)
    longest_repeated_length = 0

    # Step 3: Outer loop to consider substrings of different lengths
    for length in range(n):
        # Step 3.1: Inner loop to check each substring of the current length
        for start_index in range(n):
            # Calculate the end index to slice the substring
            end_index = start_index + length
            
            # Ensure the substring is within bounds
            if end_index <= n:
                substring = input_line[start_index:end_index]
                
                # Step 3.2: Check if the substring exists in the remainder of the string
                if substring in input_line[start_index + 1:]:
                    longest_repeated_length = length
                    break  # Exit inner loop if we found a repeated substring

    # Step 4: Output the result
    print(longest_repeated_length)

# Invoking the function
find_longest_repeated_substring()
