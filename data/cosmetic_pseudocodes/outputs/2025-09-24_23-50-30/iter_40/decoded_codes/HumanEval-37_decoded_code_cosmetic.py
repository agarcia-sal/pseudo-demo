from typing import List, TypeVar

T = TypeVar('T')

def sort_even(list_of_elements: List[T]) -> List[T]:
    bufferA: List[T] = []
    bufferB: List[T] = []
    for index in range(len(list_of_elements)):
        if index % 2 == 0:
            bufferA.append(list_of_elements[index])
        else:
            bufferB.append(list_of_elements[index])
    bufferA.sort()
    output_list: List[T] = []
    position = 0
    while position < len(bufferB):
        output_list.append(bufferA[position])
        output_list.append(bufferB[position])
        position += 1
    if len(bufferA) > len(bufferB):
        output_list.append(bufferA[-1])
    return output_list