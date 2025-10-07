from typing import Dict

def same_chars(str_alpha: str, str_beta: str) -> bool:
    set_p: Dict[str, bool] = {}
    for idx1 in range(len(str_alpha)):
        set_p[str_alpha[idx1]] = True
    set_q: Dict[str, bool] = {}
    for idx2 in range(len(str_beta)):
        set_q[str_beta[idx2]] = True
    key_p_list = list(set_p.keys())
    key_q_list = list(set_q.keys())
    if len(key_p_list) != len(key_q_list):
        return False
    for i in range(len(key_p_list)):
        if key_p_list[i] not in key_q_list:
            return False
    return True