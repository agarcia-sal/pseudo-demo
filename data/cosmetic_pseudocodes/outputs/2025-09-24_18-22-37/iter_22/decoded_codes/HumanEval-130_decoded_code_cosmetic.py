from typing import List

def tri(count: int) -> List[int]:
    if count == 0:
        return [1]
    sequence: List[int] = [1, 3]
    index = 2
    while index <= count:
        if index % 2 == 0:
            half_val = (index // 2) + 1
            sequence.append(half_val)
        else:
            prev_1 = sequence[index - 1]
            prev_2 = sequence[index - 2]
            half_sum = ((index + 3) / 2)
            new_val = prev_1 + prev_2 + half_sum
            sequence.append(new_val)
        index += 1
    return sequence