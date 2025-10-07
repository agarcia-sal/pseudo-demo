from typing import List


def circular_shift(integer_x: int, integer_shift: int) -> str:
    array_chars: List[str] = list(str(integer_x))
    length_value: int = len(array_chars)

    def recursive_concat(index_a: int, index_b: int, accumulated: List[str]) -> List[str]:
        if index_a >= length_value:
            return accumulated + array_chars[0:index_b]
        else:
            return recursive_concat(index_a + 1, index_b, accumulated + [array_chars[index_a]])

    if integer_shift > length_value:
        reversed_array: List[str] = []
        for i in range(length_value - 1, -1, -1):
            reversed_array.append(array_chars[i])
        return ''.join(reversed_array)
    else:
        return ''.join(recursive_concat(length_value - integer_shift, length_value - integer_shift, []))