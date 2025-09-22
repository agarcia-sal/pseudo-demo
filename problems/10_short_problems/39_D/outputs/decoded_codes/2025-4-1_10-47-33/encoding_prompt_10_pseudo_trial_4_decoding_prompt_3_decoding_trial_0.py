def doMain():
    # Input two strings containing space-separated integers
    t1 = input()
    t2 = input()
    
    # Split input strings into lists of strings
    tt1 = t1.split()
    tt2 = t2.split()
    
    # Initialize a result counter for different elements
    res = 0
    
    # Loop through the first three elements of the lists
    for x in range(3):
        # Convert string elements of both lists to integers
        a = int(tt1[x])
        b = int(tt2[x])
        
        # Check if the values from both lists are not equal
        if a != b:
            # Increment the result counter
            res += 1
    
    # Check the total number of different elements
    if res < 3:
        print("YES")
    else:
        print("NO")

# Main execution block
if __name__ == "__main__":
    doMain()
