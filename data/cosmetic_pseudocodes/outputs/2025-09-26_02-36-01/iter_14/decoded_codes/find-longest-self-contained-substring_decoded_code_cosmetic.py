from collections import defaultdict

class Solution:
    def maxSubstringLength(self, s: str) -> int:
        omega_freq = defaultdict(int)
        for ch in s:
            omega_freq[ch] += 1

        alpha_max = -1
        n = len(s)
        beta_i = 0

        while beta_i < n:
            chi_freq = defaultdict(int)

            # post_condition function as per pseudocode, not used directly but logic is inline below
            def post_condition(omega_map, chi_map):
                for key in chi_map:
                    if not (chi_map[key] >= omega_map[key]):
                        return False
                return True

            sigma_j = beta_i
            while sigma_j < n:
                chi_freq[s[sigma_j]] += 1
                tau_flag = True
                for c in chi_freq:
                    if chi_freq[c] < omega_freq[c]:
                        tau_flag = False
                        break

                if tau_flag and len(chi_freq) < len(omega_freq):
                    curr_len = sigma_j - beta_i + 1
                    if curr_len > alpha_max:
                        alpha_max = curr_len

                sigma_j += 1

            beta_i += 1

        return alpha_max