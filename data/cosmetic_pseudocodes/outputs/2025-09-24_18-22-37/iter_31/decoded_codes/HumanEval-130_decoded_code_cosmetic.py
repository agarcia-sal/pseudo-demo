from typing import List


def tri(param_x: int) -> List[int]:
    if param_x != 0:
        output_seq: List[int] = [1, 3]
        counter: int = 2
        while counter <= param_x:
            remainder: int = counter % 2
            if remainder == 0:
                half_plus_one: int = (counter // 2) + 1
                output_seq.append(half_plus_one)
            else:
                idx1: int = counter - 1
                idx2: int = counter - 2
                value_sum: int = output_seq[idx1] + output_seq[idx2]
                half_plus: int = (counter + 3) // 2
                output_seq.append(value_sum + half_plus)
            counter += 1
    else:
        output_seq = [1]
    return output_seq