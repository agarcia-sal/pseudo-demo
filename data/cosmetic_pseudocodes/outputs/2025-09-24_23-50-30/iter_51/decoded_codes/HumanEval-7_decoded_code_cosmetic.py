from typing import List

def filter_by_substring(collection_strings: List[str], search_text: str) -> List[str]:
    def recur(accum_result: List[str], remaining_items: List[str]) -> List[str]:
        if not remaining_items:
            return accum_result
        head, tail = remaining_items[0], remaining_items[1:]
        return recur(accum_result + [head] if search_text in head else accum_result, tail)
    return recur([], collection_strings)