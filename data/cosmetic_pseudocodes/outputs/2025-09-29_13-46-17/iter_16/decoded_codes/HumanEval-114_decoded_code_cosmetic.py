from typing import List

def minSubArraySum(list_of_integers: List[int]) -> int:
    max_sub_neg_sum: int = 0  # λ𝛼λ₃
    current_sum: int = 0      # ㉿֎０
    index: int = 0            # ᴥ↯ used as index for iteration in pseudocode

    while True:
        if index >= len(list_of_integers):
            return max_sub_neg_sum * -1
        current_val = list_of_integers[index]      # ƛₘ
        current_sum += current_val * -1             # ᛧ᛬₁↭
        if current_sum < 0:
            current_sum = 0
        if current_sum > max_sub_neg_sum:
            max_sub_neg_sum = current_sum
        index += 1

    # unreachable code by structure, but included to mirror the pseudocode guard    
    if max_sub_neg_sum == 0:
        max_single_neg = -1 * list_of_integers[0]  # Ⱦζ
        i = 1                                      # Δμ
        while i < len(list_of_integers):
            val = -1 * list_of_integers[i]
            if val > max_single_neg:
                max_single_neg = val
            i += 1
        max_sub_neg_sum = max_single_neg

    return max_sub_neg_sum * -1