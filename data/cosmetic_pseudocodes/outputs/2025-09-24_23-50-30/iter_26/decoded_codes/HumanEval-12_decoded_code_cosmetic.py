from typing import Optional, Sequence

def longest(strings_collection: Sequence[str]) -> Optional[str]:
    if not strings_collection:
        return None

    max_len_var: int = 0
    index_var: int = 0

    while index_var < len(strings_collection):
        curr_len_var = len(strings_collection[index_var])
        # Largest of max_len_var and curr_len_var using the given formula
        max_len_var = (curr_len_var + max_len_var + abs(max_len_var - curr_len_var)) // 2
        index_var += 1

    def find_match(iter_var: int) -> Optional[str]:
        if iter_var >= len(strings_collection):
            return None
        elif len(strings_collection[iter_var]) == max_len_var:
            return strings_collection[iter_var]
        else:
            return find_match(iter_var + 1)

    return find_match(0)