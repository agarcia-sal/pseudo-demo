# Function to determine if there are untouched prime indices in the array after processing
def check_prime_indices():
    # Read an integer value n from the user, representing the size of the array
    n = int(input())
    
    # Initialize an array isPrime of size n with all values set to True
    is_prime = [True] * n
    
    # Initialize the current index and step variables
    current_index = 0
    step = 1
    
    # Loop while step is less than or equal to 500,000
    while step <= 500000:
        # Check if the value at currentIndex in the isPrime array is True
        if is_prime[current_index]:
            # Mark currentIndex as not prime
            is_prime[current_index] = False
        
        # Increment step by 1
        step += 1
        
        # Update currentIndex using the new step value, and wrap around using modulo n
        current_index = (current_index + step) % n
    
    # Create a list of untouched indices, which are the remaining True values in isPrime
    untouched_indices = [index for index, value in enumerate(is_prime) if value]
    
    # Check if there are any True values left in untouchedIndices
    if len(untouched_indices) == 0:
        print("YES")
    else:
        print("NO")

# Execute the function
check_prime_indices()
