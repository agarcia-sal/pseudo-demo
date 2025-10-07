class Solution:
    def maxTotalReward(self, rewardValues):
        def bit_length_helper(n):
            count_var = 0
            while n > 0:
                n //= 2
                count_var += 1
            return count_var

        def bitwise_and_helper(a, b):
            return a & b

        def bitwise_or_helper(a, b):
            return a | b

        def bit_shift_left_helper(value, shift_amt):
            return value * (2 ** shift_amt)

        def sort_set_helper(collection):
            temp_list = []
            for elem in collection:
                inserted = False
                for index in range(len(temp_list)):
                    if elem < temp_list[index]:
                        temp_list = temp_list[:index] + [elem] + temp_list[index:]
                        inserted = True
                        break
                if not inserted:
                    temp_list.append(elem)
            return temp_list

        def unique_elements_helper(coll):
            unique_list = []
            for el in coll:
                is_found = False
                for uel in unique_list:
                    if uel == el:
                        is_found = True
                        break
                if not is_found:
                    unique_list.append(el)
            return unique_list

        temporarySet = unique_elements_helper(rewardValues)
        sortedNums = sort_set_helper(temporarySet)

        accumulator_var = 1
        recursion_index = 0

        def process_elements(seq, idx, accum):
            if idx == len(seq):
                return accum
            else:
                current_val = seq[idx]
                left_shifted_val = bit_shift_left_helper(1, current_val)
                mask_val = left_shifted_val - 1
                and_result = bitwise_and_helper(accum, mask_val)
                or_inner = bitwise_or_helper(and_result, left_shifted_val)
                new_accum = bitwise_or_helper(accum, or_inner)
                return process_elements(seq, idx + 1, new_accum)

        accumulator_var = process_elements(sortedNums, recursion_index, accumulator_var)

        bit_length_val = bit_length_helper(accumulator_var)

        return bit_length_val - 1