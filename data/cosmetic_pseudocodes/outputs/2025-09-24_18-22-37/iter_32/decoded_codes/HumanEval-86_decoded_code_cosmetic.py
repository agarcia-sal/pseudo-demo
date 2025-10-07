from typing import List

def anti_shuffle(input_string: str) -> str:
    segments: List[str] = input_string.split(' ')
    collected_sorted: List[str] = []
    index_counter: int = 0
    while index_counter < len(segments):
        current_segment: str = segments[index_counter]
        character_array: List[str] = list(current_segment)
        character_array.sort()
        reconstructed_word: str = ''.join(character_array)
        collected_sorted.append(reconstructed_word)
        index_counter += 1
    final_result: str = ''
    if collected_sorted:
        final_result = collected_sorted[0]
        iter_pos: int = 1
        while iter_pos < len(collected_sorted):
            final_result += ' ' + collected_sorted[iter_pos]
            iter_pos += 1
    return final_result