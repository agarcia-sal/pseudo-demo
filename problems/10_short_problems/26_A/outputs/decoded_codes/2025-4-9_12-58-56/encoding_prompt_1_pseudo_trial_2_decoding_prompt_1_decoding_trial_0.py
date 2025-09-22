     for currentNumber in range(1, limit + 1):
     

         for divisor in range(2, currentNumber):
         

             if currentNumber % divisor == 0:
             

               while currentNumber % divisor == 0:
                   currentNumber //= divisor
               

         if divisorCount == 2:
         

limit = int(input())
primeCount = 0

for currentNumber in range(1, limit + 1):
    divisorCount = 0

    for divisor in range(2, currentNumber):
        if currentNumber % divisor == 0:
            divisorCount += 1
            
            while currentNumber % divisor == 0:
                currentNumber //= divisor

    if divisorCount == 2:
        primeCount += 1

print(primeCount)
