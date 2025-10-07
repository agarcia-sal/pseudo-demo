from typing import List

def filter_by_prefix(collection_of_texts: List[str], lead_sequence: str) -> List[str]:
    output_accumulation: List[str] = []
    position_index: int = 0
    prefix_length: int = len(lead_sequence)
    while position_index < len(collection_of_texts):
        current_entry: str = collection_of_texts[position_index]
        does_match: bool = False
        if len(current_entry) >= prefix_length:
            segment_of_entry: str = current_entry[:prefix_length]
            if segment_of_entry == lead_sequence:
                does_match = True
        if does_match:
            output_accumulation.append(current_entry)
        position_index += 1
    return output_accumulation