def calculateRemainderAdjustment(number, divisor):
    # Calculate quotient and remainder
    quotient = number // divisor
    remainder = number % divisor
    
    # Adjust the remainder if it's greater than 0
    if remainder > 0:
        # Return adjusted value
        return remainder * (quotient + 1)
    else:
        # Return the original number if no adjustment needed
        return number

def main():
    # Read three integers from input
    n = int(input())
    m = int(input())
    s = int(input())
    
    # Adjust n and m using the calculateRemainderAdjustment function
    adjustedN = calculateRemainderAdjustment(n, s)
    adjustedM = calculateRemainderAdjustment(m, s)
    
    # Print the product of the adjusted values
    print(adjustedN * adjustedM)

# Call the main function to execute the program
main()
