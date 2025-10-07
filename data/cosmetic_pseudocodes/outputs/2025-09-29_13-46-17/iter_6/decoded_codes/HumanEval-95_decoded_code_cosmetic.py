from typing import Any, Collection


def check_dict_case(dictionary: dict[Any, Any]) -> bool:
    keys = list(dictionary.keys())
    length = len(keys)
    if length == 0:
        return False
    return _run_check(0, keys, 0, length)


def _run_check(
    state_acc: int | str,
    keys_collection: list[Any],
    idx_pos: int,
    length_limit: int,
) -> bool:
    if idx_pos >= length_limit:
        return state_acc == "upper" or state_acc == "lower"

    current_key_xX = keys_collection[idx_pos]

    if not isinstance(current_key_xX, str):
        return False

    if state_acc == 0:
        if _all_uppercase(current_key_xX):
            return _run_check("upper", keys_collection, idx_pos + 1, length_limit)
        elif _all_lowercase(current_key_xX):
            return _run_check("lower", keys_collection, idx_pos + 1, length_limit)
        else:
            return False

    condA = state_acc == "upper" and not _all_uppercase(current_key_xX)
    condB = state_acc == "lower" and not _all_lowercase(current_key_xX)
    if condA or condB:
        return False

    return _run_check(state_acc, keys_collection, idx_pos + 1, length_limit)


def _all_uppercase(strArg: str) -> bool:
    limit = len(strArg)
    return _all_uppercase_recur(strArg, 0, limit)


def _all_uppercase_recur(s: str, p: int, l: int) -> bool:
    if p >= l:
        return True
    if not _is_upper_alpha(s[p]):
        return False
    return _all_uppercase_recur(s, p + 1, l)


def _all_lowercase(strArg: str) -> bool:
    maxV = len(strArg)
    return _all_lowercase_tail(0, maxV, strArg)


def _all_lowercase_tail(position: int, limit: int, string_data: str) -> bool:
    if position >= limit:
        return True
    if not _is_lower_alpha(string_data[position]):
        return False
    return _all_lowercase_tail(position + 1, limit, string_data)


def _is_upper_alpha(char: str) -> bool:
    return "A" <= char <= "Z"


def _is_lower_alpha(char: str) -> bool:
    return "a" <= char <= "z"