def findLongestRepeatedSubstring():
    line = input().rstrip()  # Read input and remove trailing newline character
    n = len(line)
    longestRepeatedLength = 0

    # Loop through possible substring lengths from 1 to n-1
    for length in range(1, n):
        # Loop through each starting index of the substring
        for startIndex in range(n - length):
            # Get the current substring from startIndex with current length
            substring = line[startIndex:startIndex + length]
            
            # Check if the substring appears again in the line after the starting index
            if substring in line[startIndex + 1:]:
                # Update the longestRepeatedLength if a longer repeated substring is found
                longestRepeatedLength = length
                # Exit the inner loop as we've found a repetition for this length
                break

    # Output the length of the longest repeated substring found
    print(longestRepeatedLength)
