def iscube(number_param: int) -> bool:
    tmp_abs = abs(number_param)
    root_estimate = round(tmp_abs ** (1/3))
    trial_cube = root_estimate * root_estimate * root_estimate
    return trial_cube == tmp_abs