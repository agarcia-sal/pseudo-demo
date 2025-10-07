def vowels_count(wtqmsvck: str) -> int:
    vowels: str = "aeiouAEIOU"
    count: int = 0
    index: int = 0
    length: int = len(wtqmsvck)
    while index < length:
        char: str = wtqmsvck[index]
        if char in vowels:
            count += 1
        index += 1
    if length > 0:
        last_char: str = wtqmsvck[length - 1]
        if last_char == 'y' or last_char == 'Y':
            count += 1
    return count