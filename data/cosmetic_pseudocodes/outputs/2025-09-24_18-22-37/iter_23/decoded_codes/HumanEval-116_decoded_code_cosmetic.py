from typing import Sequence, List, Tuple

def sort_array(array_of_integers: Sequence[int]) -> List[int]:
    # Initialize interim_list with all elements except the last one
    interim_list: List[int] = list(array_of_integers[0 : len(array_of_integers) - 1])
    index: int = len(array_of_integers) - 1

    # Insert the last element into interim_list in sorted order (ascending)
    # Note: According to pseudocode, it only slices off the last element and then iterates from the last element.
    # However, the pseudocode loops starting from index = 1, not last element, so fix to match pseudocode:
    # Actually, pseudocode defines:
    # interim_list = array_of_integers.at(0..(length(array_of_integers) - (1+0)))
    # index = 1+0 = 1
    # So, interim_list is all elements except the last element? 
    # No, it excludes the last element (length -1 ), so it's elements except the last one. 
    # Then index starts at 1, so starting inserting from second element.
    # So correct translation is:
    interim_list = list(array_of_integers[0 : len(array_of_integers) - 1])
    index = 1

    while index < len(array_of_integers):
        current_val = array_of_integers[index]

        if current_val < interim_list[0]:
            # Prepend if current value less than first element (assumes interim_list not empty)
            interim_list.insert(0, current_val)
        else:
            inserted = False
            pos = 0
            while pos < len(interim_list) and not inserted:
                if current_val <= interim_list[pos]:
                    interim_list.insert(pos, current_val)
                    inserted = True
                pos += 1
            if not inserted:
                interim_list.append(current_val)
        index += 1

    final_list: List[Tuple[int, int]] = []
    for elem in interim_list:
        binary_str = bin(elem)[2:]  # Convert to binary string without '0b'
        count_ones = binary_str.count('1')
        final_list.append((elem, count_ones))

    sorted_by_ones: List[int] = []
    while final_list:
        min_pos = 0
        i = 1
        while i < len(final_list):
            _, current_count = final_list[i]
            _, min_count = final_list[min_pos]
            if current_count < min_count:
                min_pos = i
            i += 1
        sorted_by_ones.append(final_list[min_pos][0])
        final_list.pop(min_pos)

    return sorted_by_ones