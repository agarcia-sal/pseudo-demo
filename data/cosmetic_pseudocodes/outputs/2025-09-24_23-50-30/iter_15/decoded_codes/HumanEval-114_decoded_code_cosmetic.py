from typing import List

def minSubArraySum(array_of_values: List[int]) -> int:
    acc_val: int = 0
    max_acc: int = 0
    for idx in range(1, len(array_of_values)):
        elem = array_of_values[idx]
        neg_elem = -elem
        acc_val += neg_elem
        if acc_val < 0:
            acc_val = 0
        if acc_val > max_acc:
            max_acc = acc_val
    if max_acc == 0:
        neg_elements = [-val for val in array_of_values]
        max_acc = neg_elements[0]
        for j in range(1, len(neg_elements)):
            if neg_elements[j] > max_acc:
                max_acc = neg_elements[j]
    result: int = -max_acc
    return result