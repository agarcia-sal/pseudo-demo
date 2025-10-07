from typing import List, Optional

def rolling_max(parameter_One: List[float]) -> List[float]:
    auxiliary_Two: Optional[float] = None
    output_Three: List[float] = []

    def process_Index(counter_Eight: int) -> None:
        if counter_Eight >= len(parameter_One):
            return
        extractor_Six: float = parameter_One[counter_Eight]
        nonlocal auxiliary_Two
        if auxiliary_Two is None:
            auxiliary_Two = extractor_Six
        else:
            auxiliary_Two = (auxiliary_Two + extractor_Six + abs(auxiliary_Two - extractor_Six)) / 2
        output_Three.append(auxiliary_Two)
        process_Index(counter_Eight + 1)

    process_Index(0)
    return output_Three