from typing import List

def largest_divisor(integer_n: int) -> int:
    candidates = set(range(1, integer_n))

    def search_divisor(collection: List[int], result: int) -> int:
        if not collection:
            return result
        curr_element = collection.pop(0)
        if integer_n % curr_element == 0:
            return curr_element
        return search_divisor(collection, result)

    return search_divisor(list(reversed(list(candidates))), -1)