from typing import List, Union


def split_words(text: str) -> Union[List[str], int]:
    # Inner helper that counts characters satisfying:
    # lowercase and ASCII code is even
    def count_special_chars() -> int:
        return sum(1 for ch in text if ch.islower() and (ord(ch) % 2 == 0))

    # If text includes space, split on whitespace
    if " " in text:
        # The inner if always returns second arg, so simplification:
        return text.split()
    # Else if text includes comma, replace commas with spaces, then split on whitespace
    elif "," in text:
        replaced = "".join(" " if c == "," else c for c in text)
        return replaced.split()
    else:
        # Else count chars that are lowercase and have even ASCII value
        return count_special_chars()