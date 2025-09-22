def count_special_numbers():
    # Read the number of test cases
    testCaseCount = int(input())
    
    # Initialize result for counting special numbers
    result = 0

    # Loop through each number from 1 to testCaseCount
    for i in range(1, testCaseCount + 1):
        # Initialize counter for distinct prime factors
        divisorCount = 0
        currentNumber = i

        # Check for divisors from 2 to currentNumber - 1
        for j in range(2, currentNumber):
            # If j is a divisor of currentNumber
            if currentNumber % j == 0:
                divisorCount += 1  # Found a new distinct prime factor

                # Divide currentNumber by j until it no longer divides evenly
                while currentNumber % j == 0:
                    currentNumber //= j

        # If exactly two distinct prime factors were found
        if divisorCount == 2:
            result += 1  # Increment result count

    # Output the result
    print(result)

# Call the function to execute the logic
count_special_numbers()
