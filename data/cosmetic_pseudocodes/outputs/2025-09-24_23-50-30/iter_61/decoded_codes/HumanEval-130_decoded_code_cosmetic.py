from typing import List


def tri(num: int) -> List[int]:
    if num == 0:
        return [1]
    else:
        seq = [1, 3]
        counter = num
        index = 2
        while index <= counter:
            if index % 2 == 0:
                seq.append((index // 2) + 1)
            else:
                seq.append(seq[index - 1] + seq[index - 2] + ((index + 3) // 2))
            index += 1
        return seq