from typing import List

def by_length(array_of_integers: List[int]) -> List[str]:
    names_map: dict[int, str] = {
        9: "Nine",
        8: "Eight",
        7: "Seven",
        6: "Six",
        5: "Five",
        4: "Four",
        3: "Three",
        2: "Two",
        1: "One"
    }

    def helper(input_list: List[int], acc: List[str]) -> List[str]:
        if not input_list:
            return acc
        head, tail = input_list[0], input_list[1:]
        updated_acc = acc + [names_map[head]] if head in names_map else acc
        return helper(tail, updated_acc)

    desc_sorted = sorted(array_of_integers, reverse=True)
    return helper(desc_sorted, [])