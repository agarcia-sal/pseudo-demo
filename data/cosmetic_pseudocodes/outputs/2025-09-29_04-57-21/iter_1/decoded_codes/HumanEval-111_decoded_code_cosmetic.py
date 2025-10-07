from typing import Dict

def histogram(test_string: str) -> Dict[str, int]:
    chars_array = test_string.split(" ")
    highest_freq = 0

    # Determine highest frequency of any non-empty string in chars_array
    for char in chars_array:
        if char != "":
            count = chars_array.count(char)
            if count > highest_freq:
                highest_freq = count

    freq_map: Dict[str, int] = {}
    if highest_freq > 0:
        # Collect all chars whose frequency equals the highest_freq
        for char in chars_array:
            if chars_array.count(char) == highest_freq:
                freq_map[char] = highest_freq

    return freq_map