from typing import List

def minSubArraySum(list_of_integers: List[int]) -> int:
    acc_max: int = 0
    curr_acc: int = 0

    index: int = 0
    length: int = len(list_of_integers)
    while index < length:
        curr_acc += 0 - list_of_integers[index]
        if curr_acc < 0:
            curr_acc = 0
        if curr_acc > acc_max:
            acc_max = curr_acc
        index += 1

    if acc_max == 0:
        neg_values = [0 - val for val in list_of_integers]
        acc_max = neg_values[0]
        for i in range(1, len(neg_values)):
            if neg_values[i] > acc_max:
                acc_max = neg_values[i]

    result: int = 0 - acc_max
    return result