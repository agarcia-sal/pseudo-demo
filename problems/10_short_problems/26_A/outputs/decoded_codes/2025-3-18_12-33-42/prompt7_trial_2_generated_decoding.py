def countPrimeNumbers(limit):
    # Initialize result to count prime numbers
    result = 0
    
    # Iterate through each integer from 1 to limit
    for i in range(1, limit + 1):
        # Initialize divisor count for the current number
        divisorCount = 0
        currentNumber = i
        
        # Check potential divisors from 2 to (i - 1)
        for j in range(2, i):
            # If current number is divisible by j
            if currentNumber % j == 0:
                divisorCount += 1  # Increment divisor count
                
                # While current number is divisible by j
                while currentNumber % j == 0:
                    currentNumber //= j  # Divide current number by j
        
        # If exactly two unique divisors are found, it's a prime number
        if divisorCount == 1:  # Adjusting to count the number itself
            result += 1  # Increment the prime count
            
    return result  # Return the total count of prime numbers

# Read input (upper limit for prime counting)
t = int(input())  # Assuming input will be a valid integer

# Call the function and print the result
print(countPrimeNumbers(t))
