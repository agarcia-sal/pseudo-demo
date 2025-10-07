from typing import List

class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:

        def gen_empty_list(length: int) -> List[int]:
            # Generate a list of zeros with given length
            return [0] * length

        def get_length(coll: List[int]) -> int:
            # Return length of collection
            return len(coll)

        def front(dq: List[int]) -> int:
            return dq[0]

        def back(dq: List[int]) -> int:
            return dq[-1]

        def is_not_empty(dq: List[int]) -> bool:
            return len(dq) != 0

        def pop_front(dq: List[int]) -> int:
            first = dq[0]
            # Shift all elements left by one
            for j in range(len(dq) - 1):
                dq[j] = dq[j + 1]
            dq.pop()
            return first

        def pop_back(dq: List[int]) -> int:
            return dq.pop()

        def append_back(dq: List[int], val: int):
            dq.append(val)

        len_x = get_length(energy)
        dp_list = gen_empty_list(len_x)
        dp_list[len_x - 1] = energy[len_x - 1]
        max_val = dp_list[len_x - 1]
        queue_deque = [len_x - 1]

        def process_index(i: int, dp_ref: List[int], enrg_ref: List[int], dk: int, dq: List[int]):
            nonlocal max_val
            # Remove indices from front if they are out of k range
            while is_not_empty(dq) and (front(dq) - i >= dk):
                pop_front(dq)

            dp_ref[i] = enrg_ref[i] + dp_ref[front(dq)]

            if max_val < dp_ref[i]:
                max_val = dp_ref[i]

            # Remove from back while current dp is greater or equal
            while is_not_empty(dq) and dp_ref[i] >= dp_ref[back(dq)]:
                pop_back(dq)

            append_back(dq, i)

        def loop_descend(start: int, stop: int, act, dp_list_ref: List[int], energy_ref: List[int], k_val: int, deque_ref: List[int]):
            if start < stop:
                return
            act(start, dp_list_ref, energy_ref, k_val, deque_ref)
            loop_descend(start - 1, stop, act, dp_list_ref, energy_ref, k_val, deque_ref)

        loop_descend(len_x - 2, 0, process_index, dp_list, energy, k, queue_deque)

        return max_val