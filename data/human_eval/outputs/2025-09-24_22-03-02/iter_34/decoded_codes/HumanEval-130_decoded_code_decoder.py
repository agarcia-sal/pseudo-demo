from typing import List

def tri(n: int) -> List[int]:
    if n == 0:
        return [1]
    my_tri = [1, 3]
    i = 2
    while i <= n:
        remainder = i % 2
        if remainder == 0:
            element = 1 + i // 2
            my_tri.append(element)
        else:
            left_index = i - 1
            middle_index = i - 2
            right_value = (i + 3) // 2
            element = my_tri[left_index] + my_tri[middle_index] + right_value
            my_tri.append(element)
        i += 1
    return my_tri