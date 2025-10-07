from typing import Set

def same_chars(string_zero: str, string_one: str) -> bool:
    def chars_set(s: str) -> Set[str]:
        if s == "":
            return set()
        else:
            return {s[0]} | chars_set(s[1:])

    set_zero: Set[str] = chars_set(string_zero)
    set_one: Set[str] = chars_set(string_one)
    if not (set_zero <= set_one):
        return False
    else:
        return set_one <= set_zero