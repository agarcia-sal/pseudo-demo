def find_index_of_specific_sum():
    # Step 2: Get the absolute value of the input number
    n = abs(int(input()))
    
    # Step 3: Initialize the counter
    i = 0
    
    # Step 4: Loop indefinitely
    while True:
        # Step 4a: Calculate the sum of the first i integers
        s = (i * (i + 1)) // 2
        
        # Step 4b: Calculate the difference
        m = s - n
        
        # Step 4c: Check if the sum equals n
        if s == n:
            print(i)  # Step 4ci: Print index i
            break  # Step 4cii: Exit the loop
        
        # Step 4d: Check if the sum exceeds n
        elif s > n:
            # Step 4di: Check if the difference m is even
            if m % 2 == 0:
                print(i)  # Step 4diA: Print index i
                break  # Step 4diB: Exit the loop
        
        # Step 4e: Increment the counter
        i += 1

# Running the function to find index of specific sum
find_index_of_specific_sum()
