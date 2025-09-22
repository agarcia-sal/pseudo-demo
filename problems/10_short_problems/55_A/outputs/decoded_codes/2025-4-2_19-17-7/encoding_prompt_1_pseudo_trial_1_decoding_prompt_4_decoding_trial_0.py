def main():
    # Step 1: Input the number of elements
    n = int(input())
    
    # Step 2: Initialize a boolean list
    is_prime = [True] * n
    
    # Step 3: Initialize variables
    step = 1
    index = 0
    
    # Step 4: Loop to iterate a maximum of 500,000 times
    while step <= 500000:
        if is_prime[index]:
            is_prime[index] = False
        
        step += 1
        index = (index + step) % n  # Update the index using the given formula
    
    # Step 5: Collect remaining True values
    remaining_true = [value for value in is_prime if value]

    # Step 6: Check the result
    if not remaining_true:
        print("YES")
    else:
        print("NO")

# Call the main function to execute the code
main()
