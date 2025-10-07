def fizz_buzz(n: int) -> int:
    ns = []
    for i in range(n):
        if i % 11 == 0 or i % 13 == 0:
            ns.append(i)
    concatenated = ''.join(str(num) for num in ns)
    count_sevens = 0
    for char in concatenated:
        if char == '7':
            count_sevens += 1
    return count_sevens