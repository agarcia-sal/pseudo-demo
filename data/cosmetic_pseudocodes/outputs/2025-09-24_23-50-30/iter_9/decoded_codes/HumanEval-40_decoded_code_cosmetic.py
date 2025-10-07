from typing import List

def triples_sum_to_zero(array_tokens: List[int]) -> bool:
    length = len(array_tokens)
    position_a = 0
    while position_a < length - 2:
        position_b = position_a + 1
        while position_b < length - 1:
            total_sum = 0 - (array_tokens[position_a] + array_tokens[position_b])
            position_c = position_b + 1
            while position_c < length:
                if total_sum == array_tokens[position_c]:
                    return True
                position_c += 1
            position_b += 1
        position_a += 1
    return False