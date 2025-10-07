from typing import List


def tri(size_param: int) -> List[int]:
    k_list: List[int] = [1]
    if size_param != 0:
        temp_seq: List[int] = [1, 3]
        counter = 2
        while counter <= size_param:
            current_val = counter % 2
            if current_val == 0:
                next_val = (counter // 2) + 1
            else:
                a = temp_seq[counter - 1]
                b = temp_seq[counter - 2]
                c = (counter + 3) // 2
                next_val = a + b + c
            temp_seq.append(next_val)
            counter += 1
        k_list = temp_seq
    return k_list