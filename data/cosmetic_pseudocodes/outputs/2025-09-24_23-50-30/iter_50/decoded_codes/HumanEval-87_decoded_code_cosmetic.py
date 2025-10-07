from typing import List, Tuple


def get_row(two_dimensional_list: List[List[int]], target_integer: int) -> List[Tuple[int, int]]:
    position_stack: List[Tuple[int, int]] = []
    x_counter: int = 0

    while x_counter < len(two_dimensional_list):
        y_counter = 0
        while y_counter < len(two_dimensional_list[x_counter]):
            # Add position if element equals target_integer
            if not (two_dimensional_list[x_counter][y_counter] != target_integer):
                position_stack.append((x_counter, y_counter))
            y_counter += 1
        x_counter += 1

    def sort_by_second_desc_then_first_asc(
        input_list: List[Tuple[int, int]]
    ) -> List[Tuple[int, int]]:
        # Descending sort by second element using selection logic
        intermediate = input_list[:]
        desc_sorted: List[Tuple[int, int]] = []
        asc_sorted: List[Tuple[int, int]] = []

        temp_list = intermediate[:]
        while len(temp_list) > 0:
            max_val = float('-inf')
            max_pos = 0
            for idx in range(len(temp_list)):
                if temp_list[idx][1] > max_val:
                    max_val = temp_list[idx][1]
                    max_pos = idx
            desc_sorted.append(temp_list[max_pos])
            temp_list.pop(max_pos)

        # Ascending sort by first element using selection logic
        temp_list = desc_sorted[:]
        while len(temp_list) > 0:
            min_val = float('inf')
            min_pos = 0
            for idx in range(len(temp_list)):
                if temp_list[idx][0] < min_val:
                    min_val = temp_list[idx][0]
                    min_pos = idx
            asc_sorted.append(temp_list[min_pos])
            temp_list.pop(min_pos)

        return asc_sorted

    position_stack = sort_by_second_desc_then_first_asc(position_stack)
    return position_stack