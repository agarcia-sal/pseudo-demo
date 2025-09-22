def mark_positions():
    # Step 2: Input the integer value n
    n = int(input())
    
    # Step 3: Initialize a list `b` of size `n` filled with True values
    marked = [True] * n
    
    # Step 4: Initialization of j and i
    j = 0
    i = 1

    # Step 5: Loop while i is less than or equal to 500,000
    while i <= 500000:
        # Step 5a: Check if the position `j` is marked
        if marked[j]:
            # Step 5a(i): Mark the position
            marked[j] = False
            
        # Step 5b: Increment i
        i += 1
        
        # Step 5c: Update j with modulo to wrap around
        j = (j + i) % n

    # Step 6: Extract all True values into list x
    unmarked_positions = [value for value in marked if value]

    # Step 7: Check if list x is empty
    if len(unmarked_positions) == 0:
        # Step 7a: Output "YES"
        print("YES")
    else:
        # Step 8a: Output "NO"
        print("NO")

# Run the function
mark_positions()
