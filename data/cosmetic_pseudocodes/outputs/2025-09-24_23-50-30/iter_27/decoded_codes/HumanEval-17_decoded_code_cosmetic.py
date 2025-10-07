from typing import List

def parse_music(alpha_beta: str) -> List[List[int]]:
    gamma_delta_sigma = {'o': 4, 'o|': 2, '.|': 1}
    kappa_lambda_mu = alpha_beta.split(' ')
    xi_omicron_pi = [[gamma_delta_sigma[zeta]] for zeta in kappa_lambda_mu if zeta != '']
    return xi_omicron_pi