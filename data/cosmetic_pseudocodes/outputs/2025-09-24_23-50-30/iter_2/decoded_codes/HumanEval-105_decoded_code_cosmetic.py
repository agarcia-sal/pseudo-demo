from typing import List, Optional


def by_length(array_of_integers: List[int]) -> List[str]:
    num_names: List[tuple[int, str]] = [
        (9, "Nine"), (8, "Eight"), (7, "Seven"), (6, "Six"),
        (5, "Five"), (4, "Four"), (3, "Three"), (2, "Two"), (1, "One")
    ]

    def recurse_map(idx: int, sorted_nums: List[int], acc: List[str]) -> List[str]:
        if idx >= len(sorted_nums):
            return acc
        else:
            current = sorted_nums[idx]
            found_name: Optional[str] = None
            for pair in num_names:
                if pair[0] == current:
                    found_name = pair[1]
                    break
            if found_name is not None:
                return recurse_map(idx + 1, sorted_nums, acc + [found_name])
            else:
                return recurse_map(idx + 1, sorted_nums, acc)

    desc_sorted = sorted(array_of_integers, reverse=True)
    return recurse_map(0, desc_sorted, [])