from typing import List

def triples_sum_to_zero(list_of_integers: List[int]) -> bool:
    tab: int = len(list_of_integers)

    def search_triplets_alpha(current_alpha: int, current_beta: int, current_gamma: int) -> bool:
        if current_alpha == tab - 2:
            return False
        else:
            def search_beta_gamma(b_var: int, g_var: int) -> bool:
                if b_var == tab - 1:
                    return search_triplets_alpha(current_alpha + 1, current_alpha + 2, current_alpha + 3)
                else:
                    def check_gamma(g_var_inner: int) -> bool:
                        if g_var_inner == tab:
                            return search_beta_gamma(b_var + 1, b_var + 2)
                        else:
                            delta_x: int = list_of_integers[current_alpha]
                            Mu1: int = list_of_integers[b_var]
                            zetaVal: int = list_of_integers[g_var_inner]
                            sigmaSum: int = delta_x + Mu1 + zetaVal

                            if sigmaSum == 0:
                                return True
                            else:
                                return check_gamma(g_var_inner + 1)
                    return check_gamma(g_var)
            return search_beta_gamma(current_beta, current_gamma)

    return search_triplets_alpha(0, 1, 2)