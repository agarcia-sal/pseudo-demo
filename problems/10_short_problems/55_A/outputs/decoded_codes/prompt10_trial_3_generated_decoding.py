def main():
    # Step 1: Get user input and convert it to an integer
    n = int(input())

    # Step 2: Initialize a list of size n with all elements set to True
    active_flags = [True] * n
    
    # Step 3 & 4: Initialize the counters
    j = 0
    i = 1

    # Step 5: Loop until i exceeds 500000
    while i <= 500000:
        # Step 5a: If the current position in the list is True
        if active_flags[j]:
            # Mark the position as False
            active_flags[j] = False
        
        # Step 5b: Increment i
        i += 1
        
        # Step 5c: Update j to wrap around using modulo n
        j = (j + i) % n

    # Step 6: Create a list of positions that remain True
    true_indices = [index for index, value in enumerate(active_flags) if value]

    # Step 7: Check if there are no True values left
    if len(true_indices) == 0:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
