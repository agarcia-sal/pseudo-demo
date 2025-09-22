def do_main():
    # Step 1: Read input values
    t1 = input()
    t2 = input()

    # Step 2: Split input strings into lists
    tt1 = t1.split()
    tt2 = t2.split()

    # Step 3: Initialize result counter
    res = 0 

    # Step 4: Compare elements from the two lists
    for index in range(3):
        a = int(tt1[index])   # Convert to integer
        b = int(tt2[index])   # Convert to integer
        
        # Step 5: Increment result counter if values are different
        if a != b:
            res += 1

    # Step 6: Determine and print result
    if res < 3:
        print("YES")
    else:
        print("NO")

# Step 7: Main execution
if __name__ == "__main__":
    do_main()
