from typing import List

def sort_even(list_of_elements: List[int]) -> List[int]:
    def build_answer(even_list: List[int], odd_list: List[int], acc: List[int], idx: int) -> List[int]:
        if idx >= len(odd_list):
            if len(even_list) > len(odd_list):
                return acc + [even_list[len(even_list) - 1]]
            else:
                return acc
        else:
            return build_answer(even_list, odd_list, acc + [even_list[idx], odd_list[idx]], idx + 1)

    evens: List[int] = []
    odds: List[int] = []
    i: int = 0
    while i < len(list_of_elements):
        if i % 2 == 0:
            evens.append(list_of_elements[i])
        else:
            odds.append(list_of_elements[i])
        i += 1

    evens.sort()
    return build_answer(evens, odds, [], 0)