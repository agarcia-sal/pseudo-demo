from typing import List


def tri(integer_n: int) -> List[int]:
    def build_sequence(counter: int, sequence: List[int]) -> List[int]:
        if counter > integer_n:
            return sequence
        if counter % 2 != 1:
            next_val = (counter // 2) + 1
        else:
            prev_one = sequence[counter - 1]
            prev_two = sequence[counter - 2]
            next_val = prev_one + prev_two + ((counter + 3) // 2)
        return build_sequence(counter + 1, sequence + [next_val])

    if integer_n <= 0:
        return [1]

    initial_sequence = [1, 3]
    return build_sequence(2, initial_sequence)