class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: list[int]) -> int:
        MODULO_VALUE = 10**9 + 1

        def initializeZeroMatrix(rows: int, cols: int) -> list[list[int]]:
            return [[0] * cols for _ in range(rows)]

        transformation = initializeZeroMatrix(26, 26)

        primary_counter = 0
        while primary_counter <= 25:
            steps = 0
            limit = nums[primary_counter] if primary_counter < len(nums) else 0
            while steps < limit:
                target_index = (primary_counter + steps + 1) % 26
                transformation[primary_counter][target_index] += 1
                steps += 1
            primary_counter += 1

        def multiplyMatrices(first: list[list[int]], second: list[list[int]]) -> list[list[int]]:
            rows_count = 26
            cols_count = 26
            k_limit = 26
            product_matrix = initializeZeroMatrix(rows_count, cols_count)
            for row_iter in range(rows_count):
                for col_iter in range(cols_count):
                    sum_accumulator = 0
                    for index_k in range(k_limit):
                        temp1 = first[row_iter][index_k]
                        temp2 = second[index_k][col_iter]
                        sum_accumulator = (sum_accumulator + temp1 * temp2) % MODULO_VALUE
                    product_matrix[row_iter][col_iter] = sum_accumulator
            return product_matrix

        def powerMatrix(input_mat: list[list[int]], exp: int) -> list[list[int]]:
            def generateIdentity(size: int) -> list[list[int]]:
                id_mat = initializeZeroMatrix(size, size)
                for idx in range(size):
                    id_mat[idx][idx] = 1
                return id_mat

            result_mat = generateIdentity(26)
            base_mat = input_mat
            power_val = exp

            while power_val > 0:
                if power_val & 1:
                    result_mat = multiplyMatrices(result_mat, base_mat)
                base_mat = multiplyMatrices(base_mat, base_mat)
                power_val >>= 1

            return result_mat

        final_transform_matrix = powerMatrix(transformation, t)

        def countLetters(word: str) -> list[int]:
            counts = [0] * 26
            for ch in word:
                char_pos = ord(ch) - ord('a')
                counts[char_pos] += 1
            return counts

        initial_counts = countLetters(s)

        def multiplyVectorMatrix(vec: list[int], mat: list[list[int]]) -> list[int]:
            result_vec = [0] * 26
            for col_idx in range(26):
                val_accum = 0
                for row_idx in range(26):
                    val_accum = (val_accum + vec[row_idx] * mat[row_idx][col_idx]) % MODULO_VALUE
                result_vec[col_idx] = val_accum
            return result_vec

        transformed_counts = multiplyVectorMatrix(initial_counts, final_transform_matrix)

        def sumElements(lst: list[int]) -> int:
            aggregate = 0
            for val in lst:
                aggregate = (aggregate + val) % MODULO_VALUE
            return aggregate

        return sumElements(transformed_counts)