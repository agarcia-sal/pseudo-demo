# Begin the program
test_case_count = int(input())  # Read the number of test cases

# Initialize result for counting special numbers
result = 0

# Loop through each number from 1 to test_case_count
for i in range(1, test_case_count + 1):
    # Initialize counter for divisors
    divisor_count = 0
    current_number = i

    # Check for divisors from 2 to current_number - 1
    for j in range(2, current_number):
        # If j is a divisor of current_number
        if current_number % j == 0:
            divisor_count += 1
            
            # Divide current_number by j until it no longer divides evenly
            while current_number % j == 0:
                current_number //= j

    # If exactly two distinct prime factors were found
    if divisor_count == 2:
        result += 1

# Output the result
print(result)
