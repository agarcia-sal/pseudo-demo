from typing import List

def get_positive(unused_param: List[int]) -> List[int]:
    def helper(input_list: List[int], acc: List[int]) -> List[int]:
        if not input_list:
            return acc
        head, *tail = input_list
        if head > 0:
            return helper(tail, acc + [head])
        else:
            return helper(tail, acc)
    return helper(unused_param, [])