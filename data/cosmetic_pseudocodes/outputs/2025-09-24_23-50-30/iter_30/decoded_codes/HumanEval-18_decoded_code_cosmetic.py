def how_many_times(textual_input: str, key_sequence: str) -> int:
    tally: int = 0
    limit: int = len(textual_input) - len(key_sequence)
    cursor: int = 0
    while cursor <= limit:
        if textual_input[cursor : cursor + len(key_sequence)] == key_sequence:
            tally += 1
        cursor += 1
    return tally