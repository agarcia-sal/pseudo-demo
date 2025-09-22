def main():
    # Step 1: Read the integer value n from the user
    n = int(input())

    # Step 2: Initialize an array isPrime of size n with all values set to True
    is_prime = [True] * n

    # Step 3: Set currentIndex to 0 and step to 1
    current_index = 0
    step = 1

    # Step 4: Begin loop until step exceeds 500,000
    while step <= 500000:
        # Step 5: Check if the current index is prime
        if is_prime[current_index]:
            # Step 6: Mark the current index as not prime
            is_prime[current_index] = False
        
        # Increment step and update currentIndex
        step += 1
        current_index = (current_index + step) % n

    # Step 7: Create a list of untouchedIndices (values that remain True)
    untouched_indices = [index for index, prime in enumerate(is_prime) if prime]

    # Step 8: Check if there are any True values left
    if len(untouched_indices) == 0:
        print("YES")
    else:
        print("NO")

# Run the main function
if __name__ == "__main__":
    main()
