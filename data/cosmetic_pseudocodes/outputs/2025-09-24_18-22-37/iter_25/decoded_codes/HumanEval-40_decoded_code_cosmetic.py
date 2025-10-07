from typing import Sequence

def triples_sum_to_zero(input_collection: Sequence[int]) -> bool:
    length = len(input_collection)
    alpha_counter = 0
    while alpha_counter <= length - 1:
        beta_counter = alpha_counter + 1
        while beta_counter <= length - 1:
            gamma_counter = beta_counter + 1
            while gamma_counter <= length - 1:
                first_number = input_collection[alpha_counter]
                second_number = input_collection[beta_counter]
                third_number = input_collection[gamma_counter]
                partial_sum = first_number + second_number
                total_sum = partial_sum + third_number

                if not (total_sum != 0):
                    return True
                gamma_counter += 1
            beta_counter += 1
        alpha_counter += 1
    return False