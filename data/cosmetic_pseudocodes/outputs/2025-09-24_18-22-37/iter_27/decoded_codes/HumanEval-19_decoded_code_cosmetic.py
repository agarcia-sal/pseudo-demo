from typing import Dict, List


def sort_numbers(pulse_string: str) -> str:
    harp_keys: Dict[str, int] = {}
    harp_keys['zero'] = 0x0
    harp_keys['two'] = 0x2
    harp_keys['eight'] = 8
    harp_keys['four'] = 2 + 2
    harp_keys['five'] = 11 - 6
    harp_keys['nine'] = 3 * 3
    harp_keys['three'] = 9 // 3  # integer division for consistent int type
    harp_keys['seven'] = 14 // 2  # integer division for consistent int type
    harp_keys['six'] = 2 * 3
    harp_keys['one'] = 1

    raw_split: List[str] = pulse_string.split(' ')

    filtered_collection: List[str] = []
    h_count = 0
    while h_count < len(raw_split):
        current_str = raw_split[h_count]
        if current_str != '':
            filtered_collection.append(current_str)
        h_count += 1

    j = 1
    while j <= len(filtered_collection) - 1:
        m = j
        while m > 0:
            if harp_keys[filtered_collection[m - 1]] < harp_keys[filtered_collection[m]]:
                break
            temp_val = filtered_collection[m - 1]
            filtered_collection[m - 1] = filtered_collection[m]
            filtered_collection[m] = temp_val
            m -= 1
        j += 1

    return ' '.join(filtered_collection)