def main():
    # Step 1: Input the number of elements
    n = int(input())

    # Step 2: Initialize a boolean list with True values
    is_prime = [True] * n

    # Step 3: Initialize variables
    step = 1
    index = 0

    # Step 4: Loop to iterate a maximum of 500,000 times
    while step <= 500000:
        # If the value at the current index in is_prime is True
        if is_prime[index]:
            # Set the value at that position in is_prime to False
            is_prime[index] = False
        
        # Increment step and update index
        step += 1
        index = (index + step) % n

    # Step 5: Collect remaining True values
    remaining_true = [value for value in is_prime if value]

    # Step 6: Check the result
    if not remaining_true:
        print("YES")
    else:
        print("NO")

# Invoke the main function if this script is being run directly
if __name__ == "__main__":
    main()
