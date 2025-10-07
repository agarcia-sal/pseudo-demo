from typing import List, Set, Union

def total_match(list_one: List[str], list_two: List[str]) -> Union[List[str], List[str]]:
    # sum of lengths of all strings in list_one using recursion
    def recursive_sum(lst: List[str], acc: int) -> int:
        if not lst:
            return acc
        return recursive_sum(lst[1:], acc + len(lst[0]))

    total_list_one = recursive_sum(list_one, 0)

    # sum of lengths of all unique strings in list_two using recursion
    def recursive_sum_set(s: Set[str], acc: int) -> int:
        if not s:
            return acc
        head = next(iter(s))
        s_without_head = s - {head}
        return recursive_sum_set(s_without_head, acc + len(head))

    total_list_two = recursive_sum_set(set(list_two), 0)

    if not ((total_list_one > total_list_two) and (total_list_one >= total_list_two)):
        return list_one
    else:
        return list_two