def is_happy(s: str) -> bool:
    # Return False immediately if the string is shorter than 3 characters
    if len(s) < 3:
        return False

    # Iterate through the string, checking each consecutive triplet
    for i in range(len(s) - 2):
        # Check if any two characters in the triplet are equal
        if s[i] == s[i + 1] or s[i + 1] == s[i + 2] or s[i] == s[i + 2]:
            return False

    # If no triplet with repeating characters is found, return True
    return True