from typing import List

def mean_absolute_deviation(m_numbers_list: List[float]) -> float:
    m_length: int = len(m_numbers_list)
    if m_length == 0:
        return 0.0  # To handle empty list case robustly

    m_sum: float = 0.0
    m_index: int = 0
    while m_index < m_length:
        m_sum += m_numbers_list[m_index]
        m_index += 1
    m_mean: float = m_sum / m_length

    m_deviation_sum: float = 0.0
    m_counter: int = 0
    while m_counter < m_length:
        m_diff: float = m_numbers_list[m_counter] - m_mean
        m_abs_diff: float = -m_diff if m_diff < 0 else m_diff
        m_deviation_sum += m_abs_diff
        m_counter += 1

    m_result: float = m_deviation_sum / m_length
    return m_result