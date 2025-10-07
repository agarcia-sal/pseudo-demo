from typing import List


def tri(integer_n: int) -> List[int]:
    if integer_n == 0:
        return [1]

    sequence: List[int] = [1, 3]
    counter: int = 2

    while counter <= integer_n:
        if counter % 2 == 0:
            element = counter // 2 + 1  # integer division
            sequence.append(element)
        else:
            part_a = sequence[counter - 1]
            part_b = sequence[counter - 2]
            part_c = (counter + 3) // 2
            sequence.append(part_a + part_b + part_c)
        counter += 1

    return sequence