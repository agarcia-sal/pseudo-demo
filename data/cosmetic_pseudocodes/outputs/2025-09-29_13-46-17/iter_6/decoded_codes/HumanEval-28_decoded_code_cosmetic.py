from typing import List

def concatenate(list_of_strings: List[str]) -> str:
    def rec_convolve(queue_q: List[str], acc_result: str) -> str:
        if not queue_q:
            return acc_result
        return rec_convolve(queue_q[1:], acc_result + queue_q[0])
    return rec_convolve(list_of_strings, "")