from typing import List

def minSubArraySum(list_of_integers: List[int]) -> int:
    highest_accumulator = 0
    current_accumulator = 0
    iterator_index = 0

    while iterator_index < len(list_of_integers):
        element = list_of_integers[iterator_index]
        current_accumulator += -element  # invert sign for max subarray sum logic
        if current_accumulator >= 0:
            pass
        else:
            current_accumulator = 0
        if highest_accumulator < current_accumulator:
            highest_accumulator = current_accumulator
        iterator_index += 1

    if highest_accumulator != 0:
        return -highest_accumulator
    else:
        negative_elements: List[int] = []
        position = 0
        while position < len(list_of_integers):
            negative_elements.append(-list_of_integers[position])
            position += 1

        max_negative = negative_elements[0]
        counter = 1
        while counter < len(negative_elements):
            if max_negative < negative_elements[counter]:
                max_negative = negative_elements[counter]
            counter += 1

        return -max_negative