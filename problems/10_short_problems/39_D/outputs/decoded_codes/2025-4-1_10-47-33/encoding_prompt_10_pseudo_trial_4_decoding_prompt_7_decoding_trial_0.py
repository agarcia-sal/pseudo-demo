def doMain():
    # Assume t1 and t2 are strings containing space-separated integers.
    
    # Input two strings
    t1 = input()  # Read first input string
    t2 = input()  # Read second input string
    
    # Split input strings into lists of strings
    tt1 = t1.split()  # Convert the first string into a list of string numbers
    tt2 = t2.split()  # Convert the second string into a list of string numbers
    
    # Initialize a result counter
    res = 0  # Counter for the number of different elements
    
    # Loop through the first three elements of the lists
    for x in range(3):  # Iterate over the first three indices (0, 1, 2)
        # Convert string elements of both lists to integers
        a = int(tt1[x])  # Convert the x-th element of the first list to an integer
        b = int(tt2[x])  # Convert the x-th element of the second list to an integer
        
        # Check if the values from both lists are not equal
        if a != b:  # If the elements are different
            # Increment the result counter
            res += 1  # Increase the difference counter by 1
            
    # Check the total number of differing elements
    if res < 3:  # If there are less than 3 differences
        print("YES")  # Output "YES"
    else:
        print("NO")  # Otherwise, output "NO"

# Main execution block
if __name__ == "__main__":  # Check if this script is executed as the main program
    doMain()  # Call the main function
