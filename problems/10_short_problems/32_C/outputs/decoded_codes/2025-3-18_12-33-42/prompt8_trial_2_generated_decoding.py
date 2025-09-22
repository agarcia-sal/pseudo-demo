def calculateValue(total, size):
    quotient, remainder = divmod(total, size)
    
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return total

# Main program execution starts here
n = int(input())
m = int(input())
s = int(input())

# Call the function for both n and m and multiply the results
result = calculateValue(n, s) * calculateValue(m, s)

# Output the final result
print(result)
