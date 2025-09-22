# Start program

def mc(number, divisor):
    # Calculate the quotient and remainder
    q = number // divisor
    r = number % divisor
    
    if r > 0:
        # Return the product of the remainder and the incremented quotient
        return r * (q + 1)
    else:
        # Return the original number
        return number

# Input section
input_values = input().split()
total1 = int(input_values[0])
total2 = int(input_values[1])
divisor = int(input_values[2])

# Processing section
result1 = mc(total1, divisor)
result2 = mc(total2, divisor)

# Output section
final_product = result1 * result2
print(final_product)

# End program
