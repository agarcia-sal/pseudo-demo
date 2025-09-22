def doMain():
    # Step 1: Input two strings
    t1 = input()  # Get first string input from user
    t2 = input()  # Get second string input from user
    
    # Step 2: Split the strings into lists of substrings
    tt1 = t1.split()  # Split first string by whitespace
    tt2 = t2.split()  # Split second string by whitespace
    
    # Step 3: Initialize counter for differences
    res = 0  # Initialize difference counter
    
    # Step 4: Compare the first three elements of both lists
    for index in range(3):  # Loop through indices 0 to 2
        # Convert string elements to integers
        a = int(tt1[index])  # Convert the current element from the first string
        b = int(tt2[index])  # Convert the current element from the second string
        
        # Step 5: Check for differences
        if a != b:  # If the values are not equal
            res += 1  # Increment difference counter
    
    # Step 6: Determine the final result 
    if res < 3:  # Less than 3 differences
        print("YES")  # Print "YES"
    else:
        print("NO")  # Print "NO"

# Step 7: Main execution block
if __name__ == "__main__":  # Check if this is the main module
    doMain()  # Call the main function
