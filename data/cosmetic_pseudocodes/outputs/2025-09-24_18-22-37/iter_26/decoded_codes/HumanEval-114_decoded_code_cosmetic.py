from typing import List

def minSubArraySum(array_elements: List[int]) -> int:
    acc: int = 0
    max_acc: int = 0
    idx: int = 0
    length: int = len(array_elements)

    while idx < length:
        element_neg: int = -array_elements[idx]
        acc += element_neg
        if acc < 0:
            acc = 0
        if max_acc < acc:
            max_acc = acc
        idx += 1

    if max_acc == 0:
        candidate_values: List[int] = []
        pos: int = 0
        while pos < length:
            neg_item: int = -array_elements[pos]
            candidate_values.append(neg_item)
            pos += 1
        max_acc = candidate_values[0]
        i: int = 1
        while i < len(candidate_values):
            if max_acc < candidate_values[i]:
                max_acc = candidate_values[i]
            i += 1

    min_val: int = -max_acc
    return min_val