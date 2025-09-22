def doMain():
    # Step 1: Take two inputs
    t1 = input()
    t2 = input()

    # Step 2: Split inputs into lists of strings
    tt1 = t1.split()
    tt2 = t2.split()

    # Step 3: Initialize a result counter
    res = 0 

    # Step 4: Loop through the first three elements of the lists
    for index in range(3):
        # Convert string elements to integers
        a = int(tt1[index])
        b = int(tt2[index])
        
        # Step 5: Compare the numbers and update the counter
        if a != b:
            res += 1 

    # Step 6: Check the result counter
    if res < 3:
        print("YES")
    else:
        print("NO")

# Step 7: Execute the doMain function if this script is run as the main program
if __name__ == "__main__":
    doMain()
