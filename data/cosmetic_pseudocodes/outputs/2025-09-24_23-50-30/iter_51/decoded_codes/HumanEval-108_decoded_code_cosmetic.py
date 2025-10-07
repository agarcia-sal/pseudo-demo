from functools import reduce
from typing import List


def count_nums(sequence_of_ints: List[int]) -> int:
    def digits_sum(num: int) -> int:
        polarity = 1
        if num < 0:
            num = -num
            polarity = -1
        digits_seq = [int(ch) for ch in str(num)]
        digits_seq[0] *= polarity
        return reduce(lambda a, b: a + b, digits_seq, 0)

    sums_collection = list(map(digits_sum, sequence_of_ints))
    positive_sums = [val for val in sums_collection if val > 0]
    return len(positive_sums)