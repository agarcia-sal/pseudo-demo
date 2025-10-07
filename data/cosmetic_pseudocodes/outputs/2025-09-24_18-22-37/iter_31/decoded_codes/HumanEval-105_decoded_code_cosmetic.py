from typing import List

def by_length(given_numbers: List[int]) -> List[str]:
    num_words = {
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine"
    }

    descending_nums = sorted(given_numbers)
    reversed_descending: List[int] = []
    idx = len(descending_nums) - 1
    while idx >= 0:
        reversed_descending.append(descending_nums[idx])
        idx -= 1

    output_collection: List[str] = []
    i = 0
    while i < len(reversed_descending):
        current_val = reversed_descending[i]
        if current_val in num_words:
            output_collection.append(num_words[current_val])
        # else do nothing
        i += 1

    return output_collection