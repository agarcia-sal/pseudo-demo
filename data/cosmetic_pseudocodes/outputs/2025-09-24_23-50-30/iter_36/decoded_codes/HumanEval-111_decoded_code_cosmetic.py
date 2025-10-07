from typing import Dict, List


def histogram(test_string: str) -> Dict[str, int]:
    def countOccurrences(collection: List[str], target: str, index: int, accumulator: int) -> int:
        if index >= len(collection):
            return accumulator
        return countOccurrences(collection, target, index + 1, accumulator + (1 if collection[index] == target else 0))

    temp_dict: Dict[str, int] = {}
    split_letters: List[str] = test_string.split(' ')
    max_frequency: int = -1

    def findMaxFrequency(index: int, current_max: int) -> int:
        if index >= len(split_letters):
            return current_max
        current_item = split_letters[index]
        if current_item != "":
            freq = countOccurrences(split_letters, current_item, 0, 0)
            if freq > current_max:
                return findMaxFrequency(index + 1, freq)
            else:
                return findMaxFrequency(index + 1, current_max)
        return findMaxFrequency(index + 1, current_max)

    max_frequency = findMaxFrequency(0, max_frequency)

    if max_frequency > 0:
        def populateDictionary(index: int) -> None:
            if index >= len(split_letters):
                return
            current_item = split_letters[index]
            if current_item != "":
                freq = countOccurrences(split_letters, current_item, 0, 0)
                if freq == max_frequency:
                    temp_dict[current_item] = max_frequency
            populateDictionary(index + 1)

        populateDictionary(0)

    return temp_dict