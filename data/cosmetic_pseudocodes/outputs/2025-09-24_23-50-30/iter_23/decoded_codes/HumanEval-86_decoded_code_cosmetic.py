from typing import List


def anti_shuffle(parameter_one: str) -> str:
    container_of_segments: List[str] = []
    indexer: int = 0
    length: int = len(parameter_one)

    while indexer < length:
        if parameter_one[indexer] == ' ':
            indexer += 1
            continue

        segment = ""
        walker = indexer
        while walker < length and parameter_one[walker] != ' ':
            segment += parameter_one[walker]
            walker += 1

        container_of_segments.append(segment)
        indexer = walker

    container_of_permuted = [
        ''.join(sorted([item for item in segment]))
        for segment in container_of_segments
    ]

    output_container = ""
    for i in range(len(container_of_permuted)):
        output_container += container_of_permuted[i]
        if i < len(container_of_permuted) - 1:
            output_container += " "

    return output_container