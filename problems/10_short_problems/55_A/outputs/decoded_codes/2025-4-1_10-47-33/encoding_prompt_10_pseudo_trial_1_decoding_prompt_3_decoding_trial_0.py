def main():
    # Step 2: Input
    n = int(input())
    
    # Step 3: Initialize Boolean Array
    b = [True] * n
    
    # Step 4: Initialize Counters
    j = 0  # current index in the array
    i = 1  # current iteration number
    
    # Step 5: Loop Until Limit
    while i <= 500000:
        # Check Boolean Condition
        if b[j]:
            b[j] = False  # mark index j as processed
        i += 1
        j = (j + i) % n  # calculate next index in a circular manner
    
    # Step 6: Filter True Values
    x = [value for value in b if value]
    
    # Step 7: Output Result
    if len(x) == 0:
        print("YES")
    else:
        print("NO")

# Step 1: Start Program
if __name__ == "__main__":
    main()
