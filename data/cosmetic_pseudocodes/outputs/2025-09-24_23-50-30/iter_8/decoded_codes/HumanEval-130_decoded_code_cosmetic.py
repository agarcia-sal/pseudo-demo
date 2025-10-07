from typing import List

def tri(integer_n: int) -> List[int]:
    if integer_n <= 0:
        return [1]
    output_list: List[int] = [1, 3]
    index: int = 2
    while index <= integer_n:
        if index % 2 != 1:
            temp_val = (index // 2) + 1
        else:
            temp_val = output_list[index - 1] + output_list[index - 2] + ((index + 3) // 2)
        output_list.append(temp_val)
        index += 1
    return output_list