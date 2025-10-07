from typing import Set


def same_chars(str_u: str, str_v: str) -> bool:
    chars_u: Set[str] = set()
    for ch in str_u:
        chars_u.add(ch)

    chars_v: Set[str] = set()
    for ch in str_v:
        chars_v.add(ch)

    if characters_of_chars_v_not_in_chars_u(chars_v, chars_u) or characters_of_chars_u_not_in_chars_v(chars_u, chars_v):
        return False
    else:
        return True


def characters_of_chars_v_not_in_chars_u(set_a: Set[str], set_b: Set[str]) -> bool:
    for el in set_a:
        if el not in set_b:
            return True
    return False


def characters_of_chars_u_not_in_chars_v(set_a: Set[str], set_b: Set[str]) -> bool:
    for el in set_a:
        if el not in set_b:
            return True
    return False