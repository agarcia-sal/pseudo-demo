from typing import List

def strange_sort_list(array_of_numbers: List[int]) -> List[int]:
    while True:
        if not array_of_numbers:
            break

        temporary_flag: bool = True
        accumulator: List[int] = []

        # We only enter this loop once per call, so can manage candidates accordingly
        while True:
            if temporary_flag:
                candidate = array_of_numbers[0]
                for index in range(1, len(array_of_numbers)):
                    if array_of_numbers[index] < candidate:
                        candidate = array_of_numbers[index]
            else:
                candidate = array_of_numbers[0]
                for index in range(1, len(array_of_numbers)):
                    if candidate < array_of_numbers[index]:
                        candidate = array_of_numbers[index]

            accumulator.append(candidate)

            for index in range(len(array_of_numbers)):
                if array_of_numbers[index] == candidate:
                    del array_of_numbers[index]
                    break

            temporary_flag = not temporary_flag
            break

        # Upon first pass in pseudocode, it would GOTO start_loop again,
        # here we simulate by continuing the outer while loop. However,
        # accumulator is reset every time which contradicts pseudocode. 
        # So we need to preserve accumulator across loops and loop over start_loop properly.

    # The above implementation doesn't re-iterate properly: The pseudocode labels start_loop,
    # inside which the temp flag and accumulator are defined once.
    # But in the pseudocode, start_loop is before the check for empty and the while loop inside.
    # Actually, the pseudocode seems to say:
    # 1) while array_of_numbers not empty:
    #   - temporary_flag = True
    #   - accumulator = []
    #   - while True:
    #       - depending on temporary_flag choose min or max candidate
    #       - append candidate to accumulator
    #       - remove candidate from array_of_numbers
    #       - toggle temporary_flag
    #       - GOTO start_loop

    # The GOTO start_loop would cause the function to restart with fresh temporary_flag and accumulator,
    # so accumulator would never accumulate anything and return empty.
    # This looks contradictory.

    # Possibly the pseudocode intends to not reinitialize accumulator and flag every time,
    # so accumulator and temporary_flag should be defined outside start_loop.

    # Reinterpret code accordingly:

def strange_sort_list(array_of_numbers: List[int]) -> List[int]:
    array_of_numbers = array_of_numbers[:]  # Copy to avoid mutating input
    accumulator: List[int] = []
    temporary_flag: bool = True

    while array_of_numbers:
        if temporary_flag:
            candidate = array_of_numbers[0]
            for num in array_of_numbers[1:]:
                if num < candidate:
                    candidate = num
        else:
            candidate = array_of_numbers[0]
            for num in array_of_numbers[1:]:
                if candidate < num:
                    candidate = num

        accumulator.append(candidate)
        array_of_numbers.remove(candidate)
        temporary_flag = not temporary_flag

    return accumulator