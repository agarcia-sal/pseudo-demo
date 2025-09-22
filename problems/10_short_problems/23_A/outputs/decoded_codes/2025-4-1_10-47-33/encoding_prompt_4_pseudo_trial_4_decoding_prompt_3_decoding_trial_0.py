def find_longest_repeated_substring_length():
    # Read a line of input
    line = input().strip()
    n = len(line)
    longest_repeated_length = 0

    # Iterate through possible lengths of substrings
    for length in range(1, n):  # Start from 1 to avoid empty substring
        found_repeated = False  # Flag to check if we found a repeated substring
        # Check for repeated substrings of the current length
        for start_index in range(n - length + 1):  # Ensure we don't exceed string bounds
            # Extract the substring
            substring = line[start_index:start_index + length]

            # Check if the substring occurs again after the current index
            if substring in line[start_index + length:]:  # Check in the remaining part of the string
                longest_repeated_length = length
                found_repeated = True
                break  # Exit inner loop if a repeated substring is found
        if found_repeated:
            continue  # Break the outer loop to check for longer substrings

    # Output the length of the longest repeated substring
    print(longest_repeated_length)

# Call the function to execute when running the script
find_longest_repeated_substring_length()
