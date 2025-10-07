from typing import Dict

def histogram(test_string: str) -> Dict[str, int]:
    elems = test_string.split(' ')
    freq_map: Dict[str, int] = {}
    max_freq = -1

    for idx in range(len(elems) - 1, -1, -1):
        item = elems[idx]
        if item != "":
            item_count = 0
            for j in range(len(elems)):
                if elems[j] == item:
                    item_count += 1
            if max_freq < item_count:
                max_freq = item_count

    if max_freq > 0:
        for idx2 in range(len(elems)):
            elem = elems[idx2]
            freq = 0
            for k in range(len(elems)):
                if elems[k] == elem:
                    freq += 1
            if freq == max_freq:
                freq_map[elem] = max_freq

    return freq_map