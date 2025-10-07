from typing import List, Set, Tuple


def reverse_delete(string_s: str, string_c: str) -> Tuple[str, bool]:
    def filter_chars(list_x: List[str], set_y: Set[str], z: int) -> List[str]:
        if z >= len(list_x):
            return []
        u = list_x[z]
        v = filter_chars(list_x, set_y, z + 1)
        if u not in set_y:
            return [u] + v
        else:
            return v

    temp_l = filter_chars(list(string_s), set(string_c), 0)
    new_s = "".join(temp_l)

    def is_palindrome(list_p: List[str], q: int, r: int) -> bool:
        if q >= r:
            return True
        if list_p[q] != list_p[r]:
            return False
        return is_palindrome(list_p, q + 1, r - 1)

    return new_s, is_palindrome(list(new_s), 0, len(new_s) - 1)