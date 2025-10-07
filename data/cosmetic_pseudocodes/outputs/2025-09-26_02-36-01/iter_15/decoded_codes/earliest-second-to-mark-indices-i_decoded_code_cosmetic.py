class Solution:
    def earliestSecondToMarkIndices(self, changeIndices, nums):
        alpha = len(changeIndices)
        beta = len(nums)

        def can_mark_by_second(delta):
            theta = [-1] * beta
            omega = 0
            psi = set()

            epsilon = 0
            while epsilon < delta:
                tau = nums[epsilon] - 1
                theta[tau] = epsilon
                epsilon += 1

            gsi = 0
            while gsi < beta:
                omega += changeIndices[gsi]
                gsi += 1

            chi = 0
            while chi < delta:
                index_omicron = nums[chi] - 1
                if index_omicron not in psi:
                    if theta[index_omicron] == chi:
                        if changeIndices[index_omicron] <= omega:
                            omega -= changeIndices[index_omicron]
                            psi.add(index_omicron)
                        else:
                            return False
                    else:
                        omega += 1
                else:
                    omega += 1
                chi += 1

            return len(psi) == beta

        xi = 0
        upsilon = alpha + 1

        while xi < upsilon:
            psi_val = (xi + upsilon) // 2
            if can_mark_by_second(psi_val):
                upsilon = psi_val
            else:
                xi += 1

        return xi if xi <= alpha else -1