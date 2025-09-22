def doMain():
    # Step 1: Read two lines of input and store them in variables
    t1 = input()
    t2 = input()

    # Step 2: Split the input strings into lists of substrings
    tt1 = t1.split()
    tt2 = t2.split()

    # Step 3: Initialize a variable to count differences
    differenceCount = 0 

    # Step 4: Compare elements of the two lists
    for index in range(3):
        # Convert the substring to an integer for comparison
        a = int(tt1[index])
        b = int(tt2[index])

        # Step 5: Increment the count if the numbers are not equal
        if a != b:
            differenceCount += 1 

    # Step 6: Determine output based on the number of differences
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Step 7: Main execution block
if __name__ == "__main__":
    doMain()
