from typing import List, Optional, Union

def rolling_max(array_of_vals: List[Union[int, float]]) -> List[Union[int, float]]:
    highest_so_far: Optional[Union[int, float]] = None
    output_array: List[Union[int, float]] = []

    idx: int = 0
    while idx < len(array_of_vals):
        current_element: Union[int, float] = array_of_vals[idx]

        if highest_so_far is None:
            highest_so_far = current_element
        else:
            candidate: Union[int, float] = highest_so_far
            challenger: Union[int, float] = current_element
            if candidate >= challenger:
                highest_so_far = candidate
            else:
                highest_so_far = challenger

        output_array.append(highest_so_far)
        idx += 1

    return output_array