from typing import List, Optional, Union

def pluck(input_list: List[int]) -> Union[List[int], List[()]]:
    if len(input_list) != 0:
        evens: List[int] = [x for x in input_list if x % 2 == 0]

        if len(evens) == 0:
            return []

        min_even: int = evens[0]
        for y in evens:
            if y < min_even:
                min_even = y

        pos = 0
        for i in range(len(input_list)):
            if input_list[i] == min_even:
                pos = i
                break

        return [min_even, pos]
    else:
        return []