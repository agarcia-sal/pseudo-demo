def do_main():
    # Input two strings containing space-separated numbers
    t1 = input()
    t2 = input()
    
    # Split input strings into lists of strings
    tt1 = t1.split()
    tt2 = t2.split()
    
    # Initialize a counter for differences
    res = 0
    
    # Loop to compare the first three elements
    for x in range(3):
        # Convert string elements to integers
        a = int(tt1[x])
        b = int(tt2[x])
        
        # Compare the two integers
        if a != b:
            res += 1
    
    # Determine the result based on the count of differences
    if res < 3:
        print("YES")
    else:
        print("NO")

# Entry point for program execution
if __name__ == "__main__":
    do_main()
