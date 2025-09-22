def main():
    # Step 1: Receive user input
    t1 = input()
    t2 = input()
    
    # Step 2: Split input strings into lists of words
    tt1 = t1.split()
    tt2 = t2.split()
    
    # Step 3: Initialize the result counter
    result_counter = 0
    
    # Step 4: Loop through the first three elements of both lists
    for index in range(3):
        # Step 5: Convert string elements to integers
        a = int(tt1[index])
        b = int(tt2[index])
        
        # Step 6: Check for inequality
        if a != b:
            result_counter += 1
            
    # Step 7: Determine output based on the result counter
    if result_counter < 3:
        print("YES")
    else:
        print("NO")

# Step 8: Run Main function when the program starts
if __name__ == "__main__":
    main()
