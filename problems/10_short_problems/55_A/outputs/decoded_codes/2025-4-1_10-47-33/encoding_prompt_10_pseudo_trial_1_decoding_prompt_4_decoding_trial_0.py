def main():
    # Step 2: Input
    n = int(input())
    
    # Step 3: Initialize Boolean Array
    b = [True] * n

    # Step 4: Initialize Counters
    j = 0  # Current index in the array
    i = 1  # Current iteration number

    # Step 5: Loop Until Limit
    while i <= 500000:
        # Check Boolean Condition
        if b[j]:
            b[j] = False  # Mark index j as processed
        # Increment iteration
        i += 1
        # Calculate next index in a circular manner
        j = (j + i) % n

    # Step 6: Filter True Values
    x = [value for value in b if value]

    # Step 7: Output Result
    if len(x) == 0:
        print("YES")
    else:
        print("NO")

# Entry point of the program
if __name__ == "__main__":
    main()
