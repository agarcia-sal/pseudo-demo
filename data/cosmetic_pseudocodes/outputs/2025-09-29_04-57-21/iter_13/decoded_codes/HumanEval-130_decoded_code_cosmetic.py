from typing import List

def tri(integer_n: int) -> List[int]:
    if integer_n != 0:
        sequence: List[int] = [1, 3]

        def process(index: int) -> None:
            if index > integer_n:
                return
            if index % 2 == 0:
                sequence.append(1 + index // 2)
            else:
                sequence.append(sequence[index - 1] + sequence[index - 2] + ((index + 3) // 2))
            process(index + 1)

        process(2)
        return sequence
    return [1]