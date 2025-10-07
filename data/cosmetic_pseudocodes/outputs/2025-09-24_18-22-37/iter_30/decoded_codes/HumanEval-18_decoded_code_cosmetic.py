def how_many_times(orphaned_sequence: str, hunt_substring: str) -> int:
    found_tally = 0
    limit_index = len(orphaned_sequence) - len(hunt_substring)
    cursor = 0
    while cursor <= limit_index:
        snippet = orphaned_sequence[cursor : cursor + len(hunt_substring)]
        if snippet == hunt_substring:
            found_tally += 1
        cursor += 1
    return found_tally