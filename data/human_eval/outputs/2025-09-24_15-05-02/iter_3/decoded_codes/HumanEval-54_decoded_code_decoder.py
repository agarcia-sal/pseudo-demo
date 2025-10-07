def same_chars(s0: str, s1: str) -> bool:
    """
    Returns True if s0 and s1 contain exactly the same unique characters, False otherwise.
    """
    return set(s0) == set(s1)