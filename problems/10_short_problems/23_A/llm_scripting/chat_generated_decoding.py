from sys import stdin

def longest_repeated_substring_length(s: str) -> int:
    """
    Returns the length of the longest substring of `s` that appears at least twice.
    """
    n = len(s)
    max_length = 0  # To store the length of longest repeated substring found

    # Consider substring lengths from 1 up to n
    for length in range(1, n + 1):
        found_repeated = False  # Flag to check if any repeated substring of current length exists

        # Iterate over all possible substrings of given length
        for start in range(n - length + 1):
            current_substring = s[start:start + length]
            
            # Check if current substring appears again later in the string
            if s.find(current_substring, start + 1) != -1:
                max_length = length  # Update max_length with current length
                found_repeated = True
                break  # No need to check other substrings of this length

        # If no repeated substring found for this length, longer substrings won't be repeated
        if not found_repeated:
            break

    return max_length


if __name__ == "__main__":
    line = stdin.readline().rstrip('\n')
    result = longest_repeated_substring_length(line)
    print(result)
