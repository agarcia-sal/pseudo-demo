from typing import List

def string_sequence(integer_p: int) -> str:
    def helper(list_result: List[str], integer_index: int, integer_limit: int) -> List[str]:
        if integer_index > integer_limit:
            return list_result
        else:
            return helper(list_result + [str(integer_index)], integer_index + 1, integer_limit)
    return " ".join(helper([], 0, integer_p))