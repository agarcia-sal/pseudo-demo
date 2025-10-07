from typing import List, TypeVar

T = TypeVar('T')

def sort_even(list_of_elements: List[T]) -> List[T]:
    secondary_list: List[T] = []
    alpha: List[T] = []
    index_runner: int = 0
    while index_runner < len(list_of_elements):
        if index_runner % 2 == 0:
            alpha.append(list_of_elements[index_runner])
        else:
            secondary_list.append(list_of_elements[index_runner])
        index_runner += 1

    beta: List[T] = alpha[:]  # copy to avoid aliasing
    gamma: List[T] = secondary_list
    temp_index: int = 1
    while temp_index < len(beta):
        k = beta[temp_index]
        m = beta[temp_index - 1]
        if k < m:
            swap_flag = True
            while swap_flag:
                swap_flag = False
                for r in range(1, len(beta)):
                    if beta[r] < beta[r - 1]:
                        beta[r], beta[r - 1] = beta[r - 1], beta[r]
                        swap_flag = True
        temp_index += 1

    answer: List[T] = []
    p = 0

    while True:
        if p < len(gamma):
            answer.append(beta[p])
            answer.append(gamma[p])
        else:
            if len(beta) > len(gamma):
                answer.append(beta[p])
            break
        p += 1

    return answer