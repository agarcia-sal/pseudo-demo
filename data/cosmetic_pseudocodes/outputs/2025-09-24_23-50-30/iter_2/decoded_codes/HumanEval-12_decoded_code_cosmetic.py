from typing import List, Optional

def longest(list_of_strings: List[str]) -> Optional[str]:
    if not list_of_strings:
        return None

    candidates: List[str] = []

    def helper(idx: int) -> None:
        if idx < len(list_of_strings):
            candidates.append(list_of_strings[idx])
            helper(idx + 1)

    helper(0)

    max_len: int = 0
    for i in range(len(candidates)):
        if len(candidates[i]) > max_len:
            max_len = len(candidates[i])

    for candidate in candidates:
        if len(candidate) == max_len:
            return candidate