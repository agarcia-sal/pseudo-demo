from typing import List


def tri(scalar_m: int) -> List[int]:
    if scalar_m == 0:
        return [1]
    sequence: List[int] = [1, 3]
    counter = 2
    while counter <= scalar_m:
        if counter % 2 == 0:
            sequence.append((counter // 2) + 1)
        else:
            left_index = counter - 1
            right_index = counter - 2
            sequence.append(sequence[left_index] + sequence[right_index] + ((counter + 3) // 2))
        counter += 1
    return sequence