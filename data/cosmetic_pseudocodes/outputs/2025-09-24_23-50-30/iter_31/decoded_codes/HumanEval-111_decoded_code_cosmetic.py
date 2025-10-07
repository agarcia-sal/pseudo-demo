from typing import Dict

def histogram(input_sequence: str) -> Dict[str, int]:
    accumulator: Dict[str, int] = {}
    tokenized_elements = input_sequence.split(" ")
    peak_value = -1

    # Find the highest frequency of any non-empty element
    for element in tokenized_elements:
        if element != "":
            current_frequency = tokenized_elements.count(element)
            if current_frequency > peak_value:
                peak_value = current_frequency

    # If a peak frequency was found, collect all elements with this frequency
    if peak_value > 0:
        for element in tokenized_elements:
            if tokenized_elements.count(element) == peak_value:
                accumulator[element] = peak_value

    return accumulator