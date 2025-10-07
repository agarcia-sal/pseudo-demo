from typing import List

def derivative(formal_parameter: List[int]) -> List[int]:
    def auxiliary(result: List[int], index: int) -> List[int]:
        if index < len(formal_parameter):
            return auxiliary(result + [index * formal_parameter[index]], index + 1)
        else:
            return result
    return auxiliary([], 1)