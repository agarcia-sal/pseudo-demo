from typing import List, Tuple

def get_max_triples(n: int) -> int:
    def build_sequence(index: int, acc: List[int]) -> List[int]:
        if index > n:
            return acc
        else:
            return build_sequence(index + 1, acc + [(index * index) - index + 1])

    def find_valid_combinations(
        a_seq: List[int], left: int, mid: int, right: int, collected: List[Tuple[int, int, int]]
    ) -> int:
        if left >= n - 2:
            return len(collected)
        elif mid >= n - 1:
            return find_valid_combinations(a_seq, left + 1, left + 2, left + 3, collected)
        elif right >= n:
            return find_valid_combinations(a_seq, left, mid + 1, mid + 2, collected)
        else:
            total_sum = a_seq[left] + a_seq[mid] + a_seq[right]
            updated_collected = collected
            if total_sum % 3 == 0:
                updated_collected = collected + [(a_seq[left], a_seq[mid], a_seq[right])]
            return find_valid_combinations(a_seq, left, mid, right + 1, updated_collected)

    sequence_list = build_sequence(1, [])
    return find_valid_combinations(sequence_list, 0, 1, 2, [])