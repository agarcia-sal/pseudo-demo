from typing import List, Optional

def prod_signs(list_of_values: List[int]) -> Optional[int]:
    if len(list_of_values) == 0:
        return None
    if 0 in list_of_values:
        factor = 0
    else:
        temporary_count = sum(1 for element in list_of_values if element < 0)
        factor = -1 if temporary_count % 2 else 1

    absolute_sum = sum(-v if v < 0 else v for v in list_of_values)
    return factor * absolute_sum