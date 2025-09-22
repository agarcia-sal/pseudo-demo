def findLongestRepeatedSubstring(inputString):
    # Get the length of the input string
    stringLength = len(inputString)
    longestRepetitionLength = 0  # Initialize the longest repetition length to 0

    # Iterate over possible lengths for substrings from 1 to stringLength
    for length in range(1, stringLength):
        # Iterate over each possible starting index of the substring
        for start in range(stringLength - length):
            # Extract the substring
            substring = inputString[start:start + length]
            # Check if the substring exists later in the string
            if inputString.find(substring, start + length) != -1:
                # If found, update the longest repetition length
                longestRepetitionLength = length
                break  # Exit inner loop if a repetition is found
        else:
            continue  # Continue the outer loop
        break  # Breaks the outer loop if a repetition is found

    # Return the length of the longest repeated substring found
    return longestRepetitionLength


# Sample test cases to ensure the function works as expected
if __name__ == "__main__":
    # Test case: simple input with repeated substrings
    print(findLongestRepeatedSubstring("banana"))  # Expected output: 1 ("a", "n" are both repeated)

    # Test case: input with no repetitions
    print(findLongestRepeatedSubstring("abcde"))    # Expected output: 0 (no substrings repeat)

    # Test case: input with multiple repeated substrings
    print(findLongestRepeatedSubstring("abcabcbb"))  # Expected output: 3 ("abc" is repeated)

    # Test case: input with a long repeated substring
    print(findLongestRepeatedSubstring("abababab"))  # Expected output: 4 ("abab" is repeated)

    # Edge case: empty string
    print(findLongestRepeatedSubstring(""))           # Expected output: 0 (no substrings to repeat)

    # Edge case: single character string
    print(findLongestRepeatedSubstring("a"))          # Expected output: 0 (no substrings to repeat)
