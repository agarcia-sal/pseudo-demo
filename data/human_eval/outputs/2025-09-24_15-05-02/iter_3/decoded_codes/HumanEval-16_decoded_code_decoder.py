def count_distinct_characters(string: str) -> int:
    """
    Counts the number of distinct characters in the input string, case-insensitive.

    Args:
        string (str): The input string to process.

    Returns:
        int: The count of unique characters in the string after converting to lowercase.
    """
    lower_string = string.lower()
    unique_characters = set(lower_string)
    return len(unique_characters)