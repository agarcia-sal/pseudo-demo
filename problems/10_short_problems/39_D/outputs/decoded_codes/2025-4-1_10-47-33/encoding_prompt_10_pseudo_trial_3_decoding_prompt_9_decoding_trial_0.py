def doMain():
    # Declare variables to store input strings
    t1 = input()  # Input first string containing numbers
    t2 = input()  # Input second string containing numbers
    
    # Split the input strings into lists of strings
    tt1 = t1.split()  # Split first input string by space
    tt2 = t2.split()  # Split second input string by space
    
    res = 0  # Variable to count the number of differences
    
    # Loop to compare the first three elements
    for x in range(3):  # Loop from 0 to 2
        # Convert string elements to integers
        a = int(tt1[x])  # Convert element from first list to integer
        b = int(tt2[x])  # Convert element from second list to integer
        
        # Compare the two integers
        if a != b:  # If the two integers are not equal
            res += 1  # Increment the count of differences
    
    # Determine the result based on the count of differences
    if res < 3:  # If there are fewer than 3 differences
        print("YES")  # Print "YES"
    else:  # If there are 3 or more differences
        print("NO")  # Print "NO"

# Entry point for program execution
if __name__ == "__main__":
    doMain()  # Call the main function to execute the program
