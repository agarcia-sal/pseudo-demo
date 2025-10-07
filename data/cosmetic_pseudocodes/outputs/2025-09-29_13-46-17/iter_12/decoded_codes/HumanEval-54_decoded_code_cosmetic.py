from typing import Set


def same_chars(string_zero: str, string_one: str) -> bool:
    def power_set(s: Set[str]) -> Set[frozenset[str]]:
        # Generate the power set of set s as a set of frozensets
        if not s:
            return {frozenset()}
        elem = next(iter(s))
        rest = s - {elem}
        rest_powerset = power_set(rest)
        return rest_powerset | {subset | {elem} for subset in rest_powerset}

    set_zero = power_set(set(string_zero))
    set_one = power_set(set(string_one))
    # Check if the power sets of the characters of both strings are equal
    return set_zero == set_one