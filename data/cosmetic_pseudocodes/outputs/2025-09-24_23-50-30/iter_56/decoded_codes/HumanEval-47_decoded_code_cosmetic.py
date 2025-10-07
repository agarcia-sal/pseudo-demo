from typing import Sequence, List, Union

def median(sequence: Sequence[Union[int, float]]) -> float:
    def sorted_sequence(seq: Sequence[Union[int, float]], idx: int, acc: List[Union[int, float]]) -> List[Union[int, float]]:
        if idx < len(seq):
            # Insert element seq[idx] in sorted order into acc
            # To maintain acc sorted while appending without sorting at the end
            # But pseudocode 'acc APPEND seq[idx]' means append only, no sort
            # To comply precisely, we append all, then rely on acc later being sorted?
            # Pseudocode suggests accumulation but does not mention sorting acc.
            # But the function is named sorted_sequence and called at the start
            # So presumably it's doing a recursive copy, no sorting in the recursion?
            # However, median requires the sequence sorted, so per pseudocode,
            # the recursion just copies seq into acc, then acc is sorted sequence?
            # No. The pseudocode just appends elements, so acc holds a copy of seq.
            # That means the sequence is not sorted by this function. Possibly an error?
            # The naming suggests the pseudocode's sorted_sequence is just building a copy, not sorting.
            # But median requires sort. So the name is misleading or pseudocode incomplete.
            # To follow pseudocode exactly, we just append.
            acc.append(seq[idx])
            return sorted_sequence(seq, idx + 1, acc)
        else:
            return acc

    def half_length(len_: int) -> float:
        return len_ / 2

    def is_odd(len_: int) -> bool:
        return (len_ % 2) == 1

    def get_element(seq: Sequence[Union[int, float]], position: int) -> Union[int, float]:
        return seq[position]

    temp_sequence = sorted(sequence)
    size = len(temp_sequence)
    middle = half_length(size)

    if is_odd(size):
        return float(get_element(temp_sequence, int(middle)))
    else:
        return (get_element(temp_sequence, int(middle) - 1) + get_element(temp_sequence, int(middle))) * 0.5