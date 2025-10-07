from typing import List, Any

def sort_third(parameter_omega: List[Any]) -> List[Any]:
    local_phi: List[Any] = []
    index_alpha: int = 0
    while index_alpha < len(parameter_omega):
        if index_alpha % 3 == 0:
            local_phi.append(parameter_omega[index_alpha])
        index_alpha += 1
    sorted_phi: List[Any] = []
    count_beta: int = 0
    while count_beta < len(local_phi):
        min_value = local_phi[0]
        min_position = 0
        scan_gamma = 1
        while scan_gamma < len(local_phi):
            if local_phi[scan_gamma] < min_value:
                min_value = local_phi[scan_gamma]
                min_position = scan_gamma
            scan_gamma += 1
        sorted_phi.append(min_value)
        del local_phi[min_position]
        count_beta += 1
    idx_delta: int = 0
    while idx_delta < len(parameter_omega):
        if idx_delta % 3 == 0:
            parameter_omega[idx_delta] = sorted_phi[0]
            del sorted_phi[0]
        idx_delta += 1
    return parameter_omega