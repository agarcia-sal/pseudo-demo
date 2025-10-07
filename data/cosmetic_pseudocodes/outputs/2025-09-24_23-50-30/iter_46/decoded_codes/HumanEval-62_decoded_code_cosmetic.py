from typing import List


def derivative(list_of_coefficients: List[int]) -> List[int]:
    def helper(index: int, input_list: List[int], output_list: List[int]) -> List[int]:
        if not input_list:
            return output_list
        head, *tail = input_list
        if index == 0:
            # Skip the constant term (derivative of constant is zero)
            return helper(index + 1, tail, output_list)
        return helper(index + 1, tail, output_list + [head * index])

    return helper(0, list_of_coefficients, [])