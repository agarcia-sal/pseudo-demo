from typing import List

def strange_sort_list(list_of_integers: List[int]) -> List[int]:
    def recurse(remaining: List[int], output: List[int], toggle: bool) -> List[int]:
        if not remaining:
            return output
        candidate = min(remaining) if toggle else max(remaining)
        filtered_remaining = [x for x in remaining if x != candidate]
        return recurse(filtered_remaining, output + [candidate], not toggle)
    return recurse(list_of_integers, [], True)