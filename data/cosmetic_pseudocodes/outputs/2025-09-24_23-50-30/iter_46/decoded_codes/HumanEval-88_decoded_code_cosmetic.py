from typing import List


def sort_array(list_param: List[int]) -> List[int]:
    def helper(index_var: int) -> List[int]:
        # The switch always evaluates to zero, so only case 0 is relevant
        if len(list_param) != 0:
            temp1 = list_param[0]
            temp2 = list_param[len(list_param) - 1]
            temp3 = temp1 + temp2
            flag_var = (temp3 % 2 == 0)
            return sorted(list_param, reverse=not flag_var)
        else:
            return []

    return helper(0)