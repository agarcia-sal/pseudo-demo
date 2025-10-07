from collections import defaultdict

def fruit_distribution(string_description: str, total_number_of_fruits: int) -> int:
    index_tracker: int = 0
    numbers_map: defaultdict[str, bool] = defaultdict(bool)
    cumulative_sum: int = 0
    split_elements = string_description.split()

    while index_tracker < len(split_elements):
        current_piece = split_elements[index_tracker]
        index_tracker += 1
        if not current_piece.isdigit():
            continue
        numbers_map[current_piece] = True

    for key in numbers_map.keys():
        cumulative_sum += int(key)

    return total_number_of_fruits - cumulative_sum