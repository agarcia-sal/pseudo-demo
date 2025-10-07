from typing import List, Optional

def rolling_max(list_of_numbers: List[float]) -> List[float]:
    current_peak: Optional[float] = None
    output_sequence: List[float] = []

    for candidate_value in list_of_numbers:
        if current_peak is not None:
            current_peak = candidate_value if candidate_value > current_peak else current_peak
        else:
            current_peak = candidate_value
        output_sequence.append(current_peak)

    return output_sequence