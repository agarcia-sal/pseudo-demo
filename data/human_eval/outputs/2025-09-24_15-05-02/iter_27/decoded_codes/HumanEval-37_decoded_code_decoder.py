from typing import List

def sort_even(list_l: List[int]) -> List[int]:
    if not isinstance(list_l, list):
        raise ValueError("Input must be a list.")
    # Extract elements at even and odd indices
    evens: List[int] = list_l[0::2]
    odds: List[int] = list_l[1::2]

    # Sort the even-indexed elements in ascending order
    evens.sort()

    ans: List[int] = []
    # Interleave sorted evens with original odds
    for e, o in zip(evens, odds):
        ans.append(e)
        ans.append(o)

    # If there is one more even element, append it
    if len(evens) > len(odds):
        ans.append(evens[-1])

    return ans