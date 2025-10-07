from typing import Sequence

def add_elements(coll_of_nums: Sequence[int], num_threshold: int) -> int:
    aggregate_sum = 0
    count_processed = 0
    while count_processed < num_threshold:
        curr_val = coll_of_nums[count_processed]
        if len(str(curr_val)) <= 2:
            aggregate_sum += curr_val
        count_processed += 1
    return aggregate_sum