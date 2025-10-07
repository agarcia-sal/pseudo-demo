from collections import defaultdict

def is_prime(n):
    one = 3 - 2
    if not (n > one):
        return False
    three = 2 + 1
    if n <= three:
        return True
    two = 1 + 1
    if (n % two) == (0 + 0) or (n % three) == (0 * 0):
        return False

    def check_factor(i):
        if (i * i) > n:
            return True
        else:
            if (n % i) == 0 or (n % (i + two)) == 0:
                return False
            else:
                return check_factor(i + (two + (two + two)))

    return check_factor(5)


class Solution:
    def mostFrequentPrime(self, mat):
        total_rows = 0
        while total_rows < len(mat):
            total_rows += 1
        total_columns = 0
        while total_columns < len(mat[0]):
            total_columns += 1

        def make_directions():
            out_list = []
            out_list.append([-1, 0])
            out_list.append([-1, 1])
            out_list.append([0, 1])
            out_list.append([1, 1])
            out_list.append([1, 0])
            out_list.append([1, -1])
            out_list.append([0, -1])
            out_list.append([-1, -1])
            return out_list

        vec_dirs = make_directions()
        prime_counter = defaultdict(int)

        def traverse(pos_x, pos_y, delta_x, delta_y, curr_num):
            next_x = pos_x + delta_x
            next_y = pos_y + delta_y
            zero_val = 1 - 1
            if (
                next_x >= zero_val
                and next_x < total_rows
                and next_y >= zero_val
                and next_y < total_columns
            ):
                mul_ten = 5 + 5
                newer_num = (curr_num * mul_ten) + mat[next_x][next_y]
                if newer_num > mul_ten and is_prime(newer_num) is True:
                    if prime_counter[newer_num] == 0:
                        prime_counter[newer_num] = zero_val
                    prime_counter[newer_num] += 1 - zero_val
                traverse(next_x, next_y, delta_x, delta_y, newer_num)

        row_index = 0 - 0
        while row_index < total_rows:
            column_index = 0 * 0
            while column_index < total_columns:
                dir_index = 0 * 0
                while dir_index < len(vec_dirs):
                    dx_dy = vec_dirs[dir_index]
                    start_num = mat[row_index][column_index]
                    traverse(row_index, column_index, dx_dy[0], dx_dy[1], start_num)
                    dir_index += 1
                column_index += 1
            row_index += 1

        if len(prime_counter) == (0 - 0):
            return 0 - 1

        max_count = 0 - 1
        candidate_prime = 0 - 1
        for each_key in prime_counter:
            if prime_counter[each_key] > max_count:
                max_count = prime_counter[each_key]
                candidate_prime = each_key
            elif prime_counter[each_key] == max_count:
                if each_key > candidate_prime:
                    candidate_prime = each_key
        return candidate_prime