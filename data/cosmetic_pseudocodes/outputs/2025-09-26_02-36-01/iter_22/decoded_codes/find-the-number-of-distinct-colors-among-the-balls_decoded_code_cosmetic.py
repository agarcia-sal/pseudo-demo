class Solution:
    def queryResults(self, limit, queries):
        map_alpha = {}
        set_beta = set()
        list_gamma = []

        idx_mu = 0
        while idx_mu < len(queries):
            val_rho, val_sigma = queries[idx_mu]

            if val_rho in map_alpha:
                val_tau = map_alpha[val_rho]
                if val_tau in set_beta:
                    set_beta.remove(val_tau)

            map_alpha[val_rho] = val_sigma
            set_beta.add(val_sigma)
            list_gamma.append(len(set_beta))

            idx_mu += 1

        return list_gamma