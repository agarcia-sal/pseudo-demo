def how_many_times(str, sub):
    count = 0
    for i in range(len(str) - len(sub) + 1):
        if str[i:i+len(sub)] == sub:
            count += 1
    return count