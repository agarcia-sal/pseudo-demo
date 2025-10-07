def digitSum(s: str) -> int:
    """
    Returns the sum of ASCII codes for all uppercase characters in the input string s.
    """
    total_sum = 0
    for char in s:
        if char.isupper():
            total_sum += ord(char)
    return total_sum