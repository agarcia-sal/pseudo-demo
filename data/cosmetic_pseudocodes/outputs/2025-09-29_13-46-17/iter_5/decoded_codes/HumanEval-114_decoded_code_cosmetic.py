from typing import List

def minSubArraySum(list_of_integers: List[int]) -> int:
    def recurse_negative_max(iter_list: List[int], idx: int, cum_sum: int, peak: int) -> int:
        if idx >= len(iter_list):
            if peak == 0:
                neg_vals = [-elem for elem in iter_list]
                peak_calc = neg_vals[0]
                for j in range(1, len(neg_vals)):
                    if neg_vals[j] > peak_calc:
                        peak_calc = neg_vals[j]
                return peak_calc
            else:
                return peak
        updated_sum = cum_sum + (-iter_list[idx])
        new_sum = updated_sum if updated_sum >= 0 else 0
        new_peak = peak if new_sum <= peak else new_sum
        return recurse_negative_max(iter_list, idx + 1, new_sum, new_peak)

    result_peak = recurse_negative_max(list_of_integers, 0, 0, 0)
    minimal_value = -result_peak
    return minimal_value