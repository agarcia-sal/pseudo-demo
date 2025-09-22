def do_main():
    # Step 1: Input two strings
    t1 = input()  # Get first string input
    t2 = input()  # Get second string input
    
    # Step 2: Split the strings into lists of substrings
    tt1 = t1.split()  # Split the first string by whitespace
    tt2 = t2.split()  # Split the second string by whitespace
    
    # Step 3: Initialize counter for differences
    res = 0  # Counter for differences
    
    # Step 4: Compare the first three elements of both lists
    for index in range(3):  # Loop through the first three elements
        # Convert string elements to integers
        a = int(tt1[index])  # Convert element from first list to integer
        b = int(tt2[index])  # Convert element from second list to integer
        
        # Step 5: Check for differences
        if a != b:  # Check if the two integers are not equal
            res += 1  # Increment the difference counter
            
    # Step 6: Determine the final result 
    if res < 3:  # If less than three differences
        print("YES")  # Print "YES"
    else:
        print("NO")  # Print "NO"
        
# Step 7: Main execution block
if __name__ == "__main__":  # Check if the script is run as the main module
    do_main()  # Call the main function
