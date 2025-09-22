def countSemiPrimeNumbers(limit):
    # This will hold the count of semi-prime numbers
    result = 0  

    # Iterate through each number from 1 to limit
    for currentNumber in range(1, limit + 1):
        # To count the number of distinct prime factors
        divisorCount = 0  
        
        # Check for prime factors by iterating from 2 to currentNumber - 1
        for potentialFactor in range(2, currentNumber):
            if currentNumber % potentialFactor == 0:  # Check if divisible
                divisorCount += 1  # Found a prime factor
                
                # Reduce current number by dividing it by potentialFactor
                while currentNumber % potentialFactor == 0:
                    currentNumber //= potentialFactor  # Use integer division
                
            # If we have already found 2 distinct factors, break early
            if divisorCount > 2:
                break  

        # A semi-prime number has exactly two distinct prime factors
        if divisorCount == 2:
            result += 1  # Found a semi-prime number
    
    return result  # Return the total count of semi-prime numbers

# Main execution
limit = int(input())  # Read limit from user input
print(countSemiPrimeNumbers(limit))  # Call the function and print the result
