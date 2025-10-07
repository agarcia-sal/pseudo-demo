from typing import List, Tuple

def sort_array(param_X: List[int]) -> List[int]:
    queue_A: List[int] = sorted(param_X)
    stack_B: List[Tuple[int, int]] = []
    for index_C in range(len(queue_A)):
        variable_D: int = queue_A[index_C]
        variable_E: int = 0
        binary_repr = bin(variable_D)
        # Count '1's in binary representation from position 2 to end (0-based indexing)
        for position_F in range(2, len(binary_repr)):
            if binary_repr[position_F] == '1':
                variable_E += 1
        stack_B.append((variable_D, variable_E))

    variable_G: List[int] = []
    while stack_B:
        variable_H: Tuple[int, int] = stack_B[0]
        for index_I in range(1, len(stack_B)):
            if (stack_B[index_I][1] < variable_H[1] or
                (stack_B[index_I][1] == variable_H[1] and stack_B[index_I][0] < variable_H[0])):
                variable_H = stack_B[index_I]
        variable_G.append(variable_H[0])
        stack_B.remove(variable_H)

    return variable_G