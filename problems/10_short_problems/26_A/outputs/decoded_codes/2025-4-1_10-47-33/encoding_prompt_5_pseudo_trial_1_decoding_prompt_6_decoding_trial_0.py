# Function to check if a number is a semiprime
def is_semiprime(number):
    prime_factor_count = 0  # Counter for counting distinct prime factors
    current_number = number
    
    # Loop through all numbers starting from 2 to check for factors
    for potential_factor in range(2, current_number): 
        # If the current number is divisible by the potential factor
        if current_number % potential_factor == 0:  
            prime_factor_count += 1  # Increase the distinct prime factors count
            
            # While it's divisible, continuously divide the current number by this factor
            while current_number % potential_factor == 0:  
                current_number //= potential_factor  # Integer division
    
    return prime_factor_count == 2  # Return true if exactly two distinct prime factors found

# Take an integer input which represents the upper limit for counting semiprime numbers
upper_limit = int(input())  

semiprime_count = 0  # Initialize a counter to keep track of semiprime numbers found

# Loop through each number from 1 to upper limit
for number in range(1, upper_limit + 1):  
    if is_semiprime(number):  # Check if the current number is a semiprime
        semiprime_count += 1  # Increase the count if it is a semiprime

# Output the total count of semiprime numbers found
print(semiprime_count)  
