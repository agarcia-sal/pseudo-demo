from typing import List

def tri(integer_n: int) -> List[int]:
    if integer_n <= 0:
        return [1]

    sequence: List[int] = [1, 3]

    index: int = 2
    while index <= integer_n:
        if index % 2 == 0:
            value: int = (index // 2) + 1
            sequence.append(value)
        else:
            term_one: int = sequence[index - 1]
            term_two: int = sequence[index - 2]
            term_three: int = ((index + 3) // 2)
            sequence.append(term_one + term_two + term_three)
        index += 1

    return sequence