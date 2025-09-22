def doMain():
    # Step 1: Input two strings
    t1 = input()
    t2 = input()
    
    # Step 2: Split the strings into lists of substrings
    tt1 = t1.split()
    tt2 = t2.split()
    
    # Step 3: Initialize counter for differences
    res = 0 
    
    # Step 4: Compare the first three elements of both lists
    for index in range(3):
        # Convert string elements to integers
        a = int(tt1[index])
        b = int(tt2[index])
        
        # Step 5: Check for differences
        if a != b:
            res += 1
            
    # Step 6: Determine the final result 
    if res < 3:
        print("YES")
    else:
        print("NO")

# Step 7: Main execution block
if __name__ == "__main__":
    doMain()
