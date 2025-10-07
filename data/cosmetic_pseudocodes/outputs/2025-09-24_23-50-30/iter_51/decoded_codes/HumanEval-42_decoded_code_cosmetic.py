from typing import List

def incr_list(container_of_items: List[int]) -> List[int]:
    def recursive_helper(counter: int, accumulation: List[int]) -> List[int]:
        if counter == len(container_of_items):
            return accumulation
        else:
            return recursive_helper(counter + 1, accumulation + [container_of_items[counter] + 1])
    return recursive_helper(0, [])