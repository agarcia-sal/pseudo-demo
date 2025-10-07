class Solution:
    def minimumSum(self, grid):
        wurok = []
        idx1 = 0
        while idx1 < len(grid):
            idx2 = 0
            while idx2 < len(grid[idx1]):
                if grid[idx1] == 1 and grid[idx1][idx2] == 1:
                    plenk = (idx1, idx2)
                    wurok.append(plenk)
                idx2 += 1
            idx1 += 1

        def rect_area(points):
            if len(points) == 0:
                return 0

            def extract_first(pt_list):
                result = []
                counter = 0
                while counter < len(pt_list):
                    result.append(pt_list[counter][0])
                    counter += 1
                return result

            def extract_second(pt_list):
                result = []
                counter = 0
                while counter < len(pt_list):
                    result.append(pt_list[counter][1])
                    counter += 1
                return result

            first_elements = extract_first(points)
            second_elements = extract_second(points)

            low_i = first_elements[0]
            high_i = first_elements[0]
            counter1 = 1
            while counter1 < len(first_elements):
                if first_elements[counter1] < low_i:
                    low_i = first_elements[counter1]
                if first_elements[counter1] > high_i:
                    high_i = first_elements[counter1]
                counter1 += 1

            low_j = second_elements[0]
            high_j = second_elements[0]
            counter2 = 1
            while counter2 < len(second_elements):
                if second_elements[counter2] < low_j:
                    low_j = second_elements[counter2]
                if second_elements[counter2] > high_j:
                    high_j = second_elements[counter2]
                counter2 += 1

            width_val = (high_i + 1) + (-low_i)
            height_val = (high_j + 1) + (-low_j)

            return width_val * height_val

        minimum_value = float('inf')
        quantity = len(wurok)

        def all_combin(src_list, pick):
            def comb_rec(accum, start_idx, count_left, res):
                if count_left == 0:
                    res.append(accum)
                    return
                pos = start_idx
                while pos <= len(src_list) - count_left:
                    new_accum = accum + [src_list[pos]]
                    comb_rec(new_accum, pos + 1, count_left - 1, res)
                    pos += 1

            results_local = []
            comb_rec([], 0, pick, results_local)
            return results_local

        outer_idx = 1
        while outer_idx <= quantity - 1:
            middle_idx = outer_idx + 1
            while middle_idx <= quantity - 1:
                inner_idx = middle_idx + 1
                while inner_idx <= quantity:
                    all_comb1 = all_combin(wurok, outer_idx)

                    for subset_1 in all_comb1:
                        set_wurok = set(wurok)
                        set_sub1 = set(subset_1)
                        remain_after_1 = []
                        for element in set_wurok:
                            if element not in set_sub1:
                                remain_after_1.append(element)
                        all_comb2 = all_combin(remain_after_1, middle_idx - outer_idx)

                        for subset_2 in all_comb2:
                            set_sub2 = set(subset_2)
                            subset_3 = []
                            for element in remain_after_1:
                                if element not in set_sub2:
                                    subset_3.append(element)

                            area_one = rect_area(subset_1)
                            area_two = rect_area(subset_2)
                            area_three = rect_area(subset_3)

                            if area_one > 0 and area_two > 0 and area_three > 0:
                                combined_sum = area_one + area_two + area_three
                                if combined_sum < minimum_value:
                                    minimum_value = combined_sum

                    inner_idx += 1
                middle_idx += 1
            outer_idx += 1

        return minimum_value