def even_odd_palindrome(n):
    def is_palindrome(x):
        s = str(x)
        return s == s[::-1]

    ev, od = 0, 0
    for i in range(1, n+1):
        if is_palindrome(i):
            if i % 2 == 0:
                ev += 1
            else:
                od += 1
    return ev, od