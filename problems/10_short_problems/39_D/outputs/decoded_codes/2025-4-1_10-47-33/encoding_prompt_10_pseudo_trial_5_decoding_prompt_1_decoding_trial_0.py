def doMain():
    t1 = ""  # STRING
    t2 = ""  # STRING
    res = 0  # INTEGER

    print("Please enter the first line of numbers:")
    t1 = input()  # Read input
    print("Please enter the second line of numbers:")
    t2 = input()  # Read input

    tt1 = []  # LIST OF STRING
    tt2 = []  # LIST OF STRING

    tt1 = t1.split()  # SPLIT t1 into a list of strings
    tt2 = t2.split()  # SPLIT t2 into a list of strings

    for index in range(3):  # FOR index FROM 0 TO 2
        a = int(tt1[index])  # CONVERT tt1[index] to INTEGER
        b = int(tt2[index])  # CONVERT tt2[index] to INTEGER
        
        if a != b:  # IF a is NOT EQUAL TO b
            res += 1  # INCREMENT res by 1

    if res < 3:  # IF res is LESS THAN 3
        print("YES")
    else:  # ELSE
        print("NO")

if __name__ == "__main__":  # IF this script is executed as the main program
    doMain()  # CALL doMain()
