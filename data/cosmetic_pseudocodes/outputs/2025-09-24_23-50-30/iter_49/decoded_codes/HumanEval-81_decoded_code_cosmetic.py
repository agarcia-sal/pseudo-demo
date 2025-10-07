from typing import List, MutableSequence

def numerical_letter_grade(mutable_collection: MutableSequence[float]) -> List[str]:
    def auxiliary_reducer(current_index: int, accumulator: List[str]) -> List[str]:
        if current_index == len(mutable_collection):
            return accumulator
        value = mutable_collection[current_index]
        if value == 4.0:
            provisional = "A+"
        elif value > 3.7:
            provisional = "A"
        elif value > 3.3:
            provisional = "A-"
        elif value > 3.0:
            provisional = "B+"
        elif value > 2.7:
            provisional = "B"
        elif value > 2.3:
            provisional = "B-"
        elif value > 2.0:
            provisional = "C+"
        elif value > 1.7:
            provisional = "C"
        elif value > 1.3:
            provisional = "C-"
        elif value > 1.0:
            provisional = "D+"
        elif value > 0.7:
            provisional = "D"
        elif value > 0.0:
            provisional = "D-"
        else:
            provisional = "E"
        return auxiliary_reducer(current_index + 1, accumulator + [provisional])
    return auxiliary_reducer(0, [])