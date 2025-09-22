def mc(number, size):
    q, r = divmod(number, size)  # Calculate quotient and remainder
    if r > 0:
        return r * (q + 1)  # Adjusted value if remainder exists
    else:
        return number  # Return original number otherwise

# Read input values
n = int(input())
m = int(input())
s = int(input())

# Calculate result using the 'mc' function for both n and m
result = mc(n, s) * mc(m, s)

# Output the result
print(result)


def mc(numbers, size):
    results = []
    for number in numbers:
        q, r = divmod(number, size)
        if r > 0:
            results.append(r * (q + 1))
        else:
            results.append(number)
    return results
