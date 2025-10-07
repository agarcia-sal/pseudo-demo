from typing import List, Dict

def by_length(numbers: List[int]) -> List[str]:
    num_words: Dict[int, str] = {
        9: "Nine",
        8: "Eight",
        7: "Seven",
        6: "Six",
        5: "Five",
        4: "Four",
        3: "Three",
        2: "Two",
        1: "One",
    }
    desc_ordered: List[int] = []
    nums = numbers[:]  # Make a copy to avoid mutating input

    while len(nums) > 0:
        max_val = nums[0]
        max_idx = 0
        for i in range(1, len(nums)):
            if nums[i] > max_val:
                max_val = nums[i]
                max_idx = i
        desc_ordered.append(max_val)
        nums.pop(max_idx)

    words_list: List[str] = []
    idx: int = 0
    while idx < len(desc_ordered):
        val = desc_ordered[idx]
        if val in num_words:
            words_list.append(num_words[val])
        idx += 1

    return words_list