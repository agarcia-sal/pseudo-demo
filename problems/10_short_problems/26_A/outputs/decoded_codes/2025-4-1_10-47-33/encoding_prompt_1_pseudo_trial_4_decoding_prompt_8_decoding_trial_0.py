t = int(input())
result = 0

for i in range(1, t + 1):
    count = 0
    currentNumber = i
    
    for j in range(2, i):
        if currentNumber % j == 0:
            count += 1
            while currentNumber % j == 0:
                currentNumber //= j
                
    if count == 2:
        result += 1

print(result)
