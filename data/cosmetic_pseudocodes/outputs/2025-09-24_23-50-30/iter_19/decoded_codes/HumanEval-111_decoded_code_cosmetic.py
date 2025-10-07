from typing import Dict

def histogram(input_text: str) -> Dict[str, int]:
    frequency_map: Dict[str, int] = {}
    tokens = input_text.split(" ")
    top_frequency = 0

    index = 0
    while index < len(tokens):
        item = tokens[index]
        if item != "":
            occurrences = 0
            position = 0
            while position < len(tokens):
                if tokens[position] == item:
                    occurrences += 1
                position += 1
            if top_frequency < occurrences:
                top_frequency = occurrences
        index += 1

    if top_frequency > 0:
        index = 0
        while index < len(tokens):
            candidate = tokens[index]
            count = 0
            position = 0
            while position < len(tokens):
                if tokens[position] == candidate:
                    count += 1
                position += 1
            if count == top_frequency:
                frequency_map[candidate] = top_frequency
            index += 1

    return frequency_map