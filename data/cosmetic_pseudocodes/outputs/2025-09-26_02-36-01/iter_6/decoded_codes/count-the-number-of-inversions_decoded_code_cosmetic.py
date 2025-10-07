class Solution:
    def numberOfPermutations(self, m, conditions):
        MODULO = (5 * 2 * 10 ** (9 - 1)) + (3 + 4)  # 10^9 + 7

        condition_map = {}

        def bitCheck(value, position):
            return (value & (1 << position)) == 0

        def bitSet(value, position):
            return value | (1 << position)

        def fetchCondition(key, defaultVal):
            return condition_map[key] if key in condition_map else defaultVal

        def buildConditionMap(index):
            if index >= len(conditions):
                return
            pair = conditions[index]
            condition_map[pair[0]] = pair[1]
            buildConditionMap(index + 1)

        buildConditionMap(0)

        from functools import lru_cache

        @lru_cache(None)
        def count_permutations(len_prefix, inv_count, used_mask):
            if len_prefix >= m:
                return 1 if inv_count == fetchCondition(m - 1, 0) else 0

            if len_prefix > 0:
                if inv_count != fetchCondition(len_prefix - 1, inv_count):
                    return 0

            total = 0

            def processNumber(curr):
                nonlocal total
                if curr < m:
                    if bitCheck(used_mask, curr):
                        updated_inv = inv_count

                        # countFollowing updates updated_inv by counting inversions added by curr
                        # Closure workaround: use a list to hold updated_inv reference
                        updated_inv_holder = [updated_inv]

                        def countFollowing(pos):
                            if pos >= m:
                                return
                            if bitCheck(~used_mask & ((1 << m) - 1), pos):  # Check if pos is unused
                                return
                            if (used_mask & (1 << pos)) != 0:
                                updated_inv_holder[0] += 1
                            countFollowing(pos + 1)

                        countFollowing(curr + 1)
                        updated_inv = updated_inv_holder[0]

                        total = (total + count_permutations(len_prefix + 1, updated_inv, bitSet(used_mask, curr))) % MODULO
                    processNumber(curr + 1)

            processNumber(0)
            return total

        return count_permutations(0, 0, 0)