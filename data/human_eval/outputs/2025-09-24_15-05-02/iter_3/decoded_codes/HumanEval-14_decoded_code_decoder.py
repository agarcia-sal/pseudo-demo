def all_prefixes(text: str) -> list[str]:
    """
    Returns a list of all prefixes of the input string.
    Each prefix is a substring from the start up to position i+1.
    """
    return [text[:i+1] for i in range(len(text))]