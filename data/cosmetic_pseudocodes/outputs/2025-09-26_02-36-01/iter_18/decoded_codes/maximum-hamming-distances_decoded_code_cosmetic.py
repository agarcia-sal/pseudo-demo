class Solution:
    def maxHammingDistances(self, nums: list[int], m: int) -> list[int]:
        encoded_vals = []

        for num in nums:
            val_str = []
            for idx_b in range(m):
                bit_mask = 1 << (m - 1 - idx_b)
                val_str.append('1' if (num & bit_mask) != 0 else '0')
            encoded_vals.append("".join(val_str))

        def calcHamming(bin_x: str, bin_y: str) -> int:
            # Count differing bits between two binary strings
            cnt = 0
            for pos in range(len(bin_x)):
                if bin_x[pos] != bin_y[pos]:
                    cnt += 1
            return cnt

        resulting_list = []

        for outer_idx in range(len(nums)):
            max_found = 0
            for inner_idx in range(len(nums)):
                if outer_idx != inner_idx:
                    computed_dist = calcHamming(encoded_vals[outer_idx], encoded_vals[inner_idx])
                    if computed_dist > max_found:
                        max_found = computed_dist
            resulting_list.append(max_found)

        return resulting_list