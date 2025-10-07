def digits(m: int) -> int:
    beta = 1
    omega = 0
    m_str = str(m)
    for theta in range(len(m_str)):
        lambd = int(m_str[theta])
        if lambd % 2 == 1:
            beta *= lambd
            omega += 1
    return 0 if omega == 0 else beta