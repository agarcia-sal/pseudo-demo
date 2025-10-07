from typing import List, Union

def intersperse(arr_numeric: List[Union[int, float]], sep_symbol: Union[int, float]) -> List[Union[int, float]]:
    output_sequence: List[Union[int, float]] = []
    if len(arr_numeric) == 0:
        return output_sequence

    idx: int = 0
    while idx < len(arr_numeric) - 1:
        output_sequence.append(arr_numeric[idx])
        output_sequence.append(sep_symbol)
        idx += 1

    output_sequence.append(arr_numeric[len(arr_numeric) - 1])
    return output_sequence