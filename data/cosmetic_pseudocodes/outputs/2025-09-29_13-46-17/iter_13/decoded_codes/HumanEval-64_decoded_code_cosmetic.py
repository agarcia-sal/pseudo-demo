from typing import List

def vowels_count(string_input: str) -> int:
    vowels: str = "AEIOUaeiou"
    # sum 1 for each character in string_input if it's in vowels
    count: int = sum(1 if char in vowels else 0 for char in string_input)
    # if last character is 'y' or 'Y', add 1 to count
    if string_input and string_input[-1] in ('y', 'Y'):
        count += 1
    return count