def doMain():
    # Read two lines of input
    t1 = input()
    t2 = input()
    
    # Split the two input strings by space into lists
    tt1 = t1.split()
    tt2 = t2.split()
    
    # Initialize a counter for differences
    res = 0 
    
    # Loop through the first three elements of both lists
    for x in range(3):
        # Convert string elements to integers
        a = int(tt1[x])
        b = int(tt2[x])
        
        # Check if the integers are different
        if a != b:
            # Increment the difference counter
            res += 1
    
    # Check the number of differences
    if res < 3:
        print("YES")
    else:
        print("NO")

# Main execution starts here
if __name__ == "__main__":
    doMain()


     1 2 3
     1 2 3
     

     1 2 3
     4 5 6
     

     5 5 5
     5 5 5
     

     1 0 1
     0 1 0
     

     999 500 250
     999 500 251
     

     -2147483648 -2147483648 -2147483648
     -2147483648 -2147483648 -2147483647
     

     2147483647 2147483647 2147483647
     2147483647 2147483647 2147483646
     