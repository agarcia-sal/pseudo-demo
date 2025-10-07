class Solution:
    def maximumTotalDamage(self, power):
        tally = {}
        for item in power:
            tally[item] = tally.get(item, 0) + 1

        keys_sorted = sorted(tally.keys())
        record = {}

        def compute_dp(pos):
            if pos < 0:
                return 0
            if pos in record:
                return record[pos]

            current_val = keys_sorted[pos]
            omit_cur = compute_dp(pos - 1)
            inc_cur = current_val * tally[current_val]

            scan_index = pos - 1
            while scan_index >= 0 and keys_sorted[scan_index] >= current_val - 2:
                scan_index -= 1

            if scan_index >= 0:
                inc_cur += compute_dp(scan_index)

            chosen_val = inc_cur if inc_cur >= omit_cur else omit_cur
            record[pos] = chosen_val
            return chosen_val

        return compute_dp(len(keys_sorted) - 1)