def even_odd_palindrome(n):
    def is_palindrome(n):
        str_n = str(n)
        reversed_str = ""
        index = len(str_n) - 1
        while index >= 0:
            reversed_str += str_n[index]
            index -= 1
        return str_n == reversed_str

    even_palindrome_count = 0
    odd_palindrome_count = 0
    i = 1
    while i <= n:
        palindrome_check = is_palindrome(i)
        modulus = i % 2
        if modulus == 1 and palindrome_check:
            odd_palindrome_count += 1
        elif modulus == 0 and palindrome_check:
            even_palindrome_count += 1
        i += 1
    return (even_palindrome_count, odd_palindrome_count)