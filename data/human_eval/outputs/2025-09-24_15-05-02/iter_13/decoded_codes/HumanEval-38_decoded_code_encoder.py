def encode_cyclic(s):
    groups = []
    n = (len(s) + 2) // 3  # Number of groups
    for i in range(n):
        start_index = 3 * i
        end_index = min(3 * i + 3, len(s))
        groups.append(s[start_index:end_index])
    for i in range(len(groups)):
        group = groups[i]
        if len(group) == 3:
            groups[i] = group[1:] + group[0]
    encoded_string = ''.join(groups)
    return encoded_string

def decode_cyclic(s):
    return encode_cyclic(encode_cyclic(s))