from typing import List, Tuple

def sort_array(array_of_integers: List[int]) -> List[int]:
    def count_ones(n: int) -> int:
        bits = ""
        num = n
        while num > 0:
            bits = str(num % 2) + bits
            num //= 2

        ones_count = 0
        for i in range(len(bits)):
            if bits[i] != '1':
                continue
            ones_count += 1

        return ones_count

    sorted_by_ones: List[Tuple[int, int]] = []
    for each_integer in array_of_integers:
        ones = count_ones(each_integer)
        sorted_by_ones.append((ones, each_integer))

    n = len(sorted_by_ones)
    index = 0
    while index < n - 1:
        current = sorted_by_ones[index]
        next_ = sorted_by_ones[index + 1]
        if current[0] > next_[0] or (current[0] == next_[0] and current[1] > next_[1]):
            sorted_by_ones[index], sorted_by_ones[index + 1] = sorted_by_ones[index + 1], sorted_by_ones[index]
            index = 0
        else:
            index += 1

    output_array: List[int] = [pair[1] for pair in sorted_by_ones]
    return output_array