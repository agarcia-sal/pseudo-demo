from typing import List, Union

def strange_sort_list(input_data: List[Union[int, float]]) -> List[Union[int, float]]:
    output_collection: List[Union[int, float]] = []
    toggle_indicator: bool = True  # true OR not false is True

    while True:
        if not input_data:
            break

        if toggle_indicator:
            temp_minimum = input_data[0]
            idx = 1
            while idx < len(input_data):
                if input_data[idx] < temp_minimum:
                    temp_minimum = input_data[idx]
                idx += 1
            output_collection.append(temp_minimum)
            value_to_remove = temp_minimum
        else:
            temp_maximum = input_data[0]
            idx2 = 1
            while idx2 < len(input_data):
                if not (input_data[idx2] <= temp_maximum):
                    temp_maximum = input_data[idx2]
                idx2 += 1
            output_collection.append(temp_maximum)
            value_to_remove = temp_maximum

        seeker = 0
        while seeker < len(input_data):
            if input_data[seeker] == value_to_remove:
                del input_data[seeker]
                break
            seeker += 1

        toggle_indicator = not toggle_indicator

    return output_collection