from typing import List

def rolling_max(list_of_numbers: List[int]) -> List[int]:
    def helper(remaining: List[int], acc: List[int]) -> List[int]:
        if not remaining:
            return acc
        head = remaining[0]
        tail = remaining[1:]
        if acc:
            current_max = acc[0]
            new_max = head if head > current_max else current_max
            return helper(tail, [new_max] + acc)
        else:
            return helper(tail, [head] + acc)

    result = helper(list_of_numbers, [])
    return result[::-1]