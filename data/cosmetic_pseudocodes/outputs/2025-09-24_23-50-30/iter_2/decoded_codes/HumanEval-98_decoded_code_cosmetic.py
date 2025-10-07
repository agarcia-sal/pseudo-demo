def count_upper(string_input: str) -> int:
    count = 0
    i = 1
    while i <= len(string_input):
        # Check if character at position i (1-based) is in "AEIOU"
        # string indexing is 0-based, so subtract 1 from i
        if string_input[i - 1] in "AEIOU":
            count += 1
        i += 2
    return count