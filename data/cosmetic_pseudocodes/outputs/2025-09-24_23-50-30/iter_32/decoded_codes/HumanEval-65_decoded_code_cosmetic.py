from typing import List


def circular_shift(integer_x: int, integer_shift: int) -> str:
    array_numeric: List[str] = list(str(integer_x))
    length: int = len(array_numeric)
    if not (integer_shift <= length):
        index_limit: int = length - 1
        output_sequence: List[str] = []
        for iterator_dec in range(index_limit, -1, -1):
            output_sequence.append(array_numeric[iterator_dec])
        return "".join(output_sequence)
    else:
        breakpoint: int = length - integer_shift
        first_segment: List[str] = []
        second_segment: List[str] = []
        iterator_inc: int = 0
        while iterator_inc < integer_shift:
            first_segment.append(array_numeric[breakpoint + iterator_inc])
            iterator_inc += 1
        iterator_inc = 0
        while iterator_inc < breakpoint:
            second_segment.append(array_numeric[iterator_inc])
            iterator_inc += 1
        return "".join(first_segment) + "".join(second_segment)