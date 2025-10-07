from collections import defaultdict

class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:
        n = len(s)

        def dfs(alpha: int) -> int:
            if alpha >= n:
                return 0

            map_omega = dict()
            count_sigma = defaultdict(int)
            result_phi = n - alpha  # worst case: each remaining character as a substring

            # Adjust counts when removing a previous character at index beta
            def recurse_gamma(beta: int, e: str) -> None:
                if e in map_omega and map_omega[e] != 0:
                    count_sigma[map_omega[e]] -= 1
                    if count_sigma[map_omega[e]] == 0:
                        del count_sigma[map_omega[e]]

            # Add counts when adding a new character e
            def augment_delta(e: str) -> None:
                map_omega[e] = map_omega.get(e, 0) + 1
                count_sigma[map_omega[e]] = count_sigma.get(map_omega[e], 0) + 1

            i = alpha
            while i <= n - 1:
                recurse_gamma(i, s[i])
                augment_delta(s[i])

                if len(count_sigma) == 1:
                    temp_kappa = 1 + dfs(i + 1)
                    if temp_kappa < result_phi:
                        result_phi = temp_kappa
                i += 1

            return result_phi

        return dfs(0)