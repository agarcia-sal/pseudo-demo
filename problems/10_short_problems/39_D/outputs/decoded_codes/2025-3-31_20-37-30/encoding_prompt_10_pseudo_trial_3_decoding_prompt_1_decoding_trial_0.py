def doMain():
    # Step 1: Input two strings
    t1 = input()  # GET user input
    t2 = input()  # GET user input
    
    # Step 2: Split the strings into lists of substrings
    tt1 = t1.split()  # SPLIT t1 by whitespace
    tt2 = t2.split()  # SPLIT t2 by whitespace
    
    # Step 3: Initialize counter for differences
    res = 0  # Declare integer res
    
    # Step 4: Compare the first three elements of both lists
    for index in range(3):  # FROM 0 TO 2 DO
        # Convert string elements to integers
        a = int(tt1[index])  # CONVERT tt1[index] to integer
        b = int(tt2[index])  # CONVERT tt2[index] to integer
        
        # Step 5: Check for differences
        if a != b:  # IF a is NOT equal to b THEN
            res += 1  # INCREMENT res by 1
            
    # Step 6: Determine the final result 
    if res < 3:  # IF res is LESS than 3 THEN
        print("YES")  # PRINT "YES"
    else:
        print("NO")  # PRINT "NO"

# Step 7: Main execution block
if __name__ == "__main__":  # IF __name__ is "main" THEN
    doMain()  # CALL doMain()
