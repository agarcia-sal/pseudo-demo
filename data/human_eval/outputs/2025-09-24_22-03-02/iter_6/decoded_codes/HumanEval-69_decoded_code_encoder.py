from typing import List

def search(lst: List[int]) -> int:
    frequency_list = [0] * (max(lst) + 1)
    for number in lst:
        frequency_list[number] += 1
    answer = -1
    for index in range(1, len(frequency_list)):
        if frequency_list[index] >= index:
            answer = index
    return answer