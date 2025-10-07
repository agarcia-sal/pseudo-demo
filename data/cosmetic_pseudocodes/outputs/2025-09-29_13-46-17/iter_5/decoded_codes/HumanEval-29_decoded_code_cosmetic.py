from typing import List

def filter_by_prefix(mixedCollection: List[str], keySequence: str) -> List[str]:
    matchedResults: List[str] = []

    def check_and_collect(recCollection: List[str], idx: int) -> List[str]:
        if idx >= len(recCollection):
            return matchedResults

        candidate = recCollection[idx]
        prefixLength = len(keySequence)

        def is_prefix(s: str, pre: str, pos: int) -> bool:
            if pos >= prefixLength:
                return True
            if pos < len(s) and s[pos] == pre[pos]:
                return is_prefix(s, pre, pos + 1)
            return False

        if is_prefix(candidate, keySequence, 0):
            matchedResults.append(candidate)

        return check_and_collect(recCollection, idx + 1)

    return check_and_collect(mixedCollection, 0)