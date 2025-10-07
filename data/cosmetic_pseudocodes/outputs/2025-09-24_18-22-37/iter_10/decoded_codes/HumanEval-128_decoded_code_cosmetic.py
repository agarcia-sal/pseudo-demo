from typing import List, Optional


def prod_signs(array_of_integers: List[int]) -> Optional[int]:
    if array_of_integers:
        has_zero_flag = False
        temp_index = 0
        while temp_index < len(array_of_integers) and not has_zero_flag:
            if array_of_integers[temp_index] == 0:
                has_zero_flag = True
            temp_index += 1

        if has_zero_flag:
            sign_product = 0
        else:
            temp_neg_count = 0
            iter_var = 0
            while iter_var < len(array_of_integers):
                if array_of_integers[iter_var] < 0:
                    temp_neg_count += 1
                iter_var += 1

            exponent_val = temp_neg_count
            sign_product = 1
            for _ in range(1, exponent_val + 1):
                sign_product *= -1

        total_magnitude = 0
        sum_index = 0
        while sum_index < len(array_of_integers):
            total_magnitude += abs(array_of_integers[sum_index])
            sum_index += 1

        return sign_product * total_magnitude

    return None