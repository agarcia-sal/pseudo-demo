from typing import Iterable, List, Optional


def rolling_max(aggregate_values: Iterable[int]) -> List[int]:
    tracking_peak: Optional[int] = None
    output_sequence: List[int] = []

    for current_value in aggregate_values:
        if tracking_peak is None:
            tracking_peak = current_value
        else:
            if current_value > tracking_peak:
                tracking_peak = current_value
        output_sequence.append(tracking_peak)
    return output_sequence