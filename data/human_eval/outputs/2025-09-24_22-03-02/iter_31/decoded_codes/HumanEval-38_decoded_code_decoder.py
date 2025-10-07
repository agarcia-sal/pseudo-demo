def encode_cyclic(s: str) -> str:
    groups = []
    length_s = len(s)
    upper_limit = (length_s + 2) // 3
    for i in range(upper_limit):
        start_index = 3 * i
        end_index = start_index + 3
        if end_index > length_s:
            end_index = length_s
        substring = s[start_index:end_index]
        groups.append(substring)

    for k in range(len(groups)):
        group = groups[k]
        if len(group) == 3:
            new_group = group[1:3] + group[0]
            groups[k] = new_group

    result = ''.join(groups)
    return result

def decode_cyclic(s: str) -> str:
    encoded_once = encode_cyclic(s)
    encoded_twice = encode_cyclic(encoded_once)
    return encoded_twice