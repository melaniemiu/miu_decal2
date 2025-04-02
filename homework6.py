

# Question 1
import numpy as np

def isPrime(n):
    if n < 2: #Rule 1: prime numbers MUST be greater than 2.
        return False
    
    for i in range(2, int(n**0.5)+1):
        #Checks if n has any factors from sqrt(n) to 2.

        if n % i == 0:
        #If n is divisible by i, then it is not a prime number.
        #B/c if 2 numbers a and b are multiplied, a larger numbver than n results 
        #so at least ONE number must be smaller than n.

            return False
    else:
        return True

def containsaPrime(arr):
    result = []
    for row in arr:
        if any(isPrime(n) for n in row):
            result.append(row)
    return np.array(result)

arr = np.array([[2, 3, 5], [4, 6, 8], [11, 13, 17], [7, 10, 13]])
print(containsaPrime(arr))


# Question 2.1

import numpy as np

checkerboard = np.zeros((8,8))
print(checkerboard)


# Question 2.2

def checkerboard_oddrows():
    arr = np.zeros((8,8)) # Makes an 8x8 filled with zeroes.
    for i in range(8): # Tells Python to look at the rows
        if i % 2 != 0: # Identifies the odd rows.
            arr[i] = [1,0,1,0,1,0,1,0] # Makes odd rows follow this pattern.
    return arr

print(checkerboard_oddrows())

# Question 2.3

def checkerboard_evenrows():
    arr = np.zeros((8,8)) # Makes an 8x8 filled with zeroes.
    for m in range(8): # Tells Python to look at the rows
        if m % 2 == 0: # Identifies the even rows.
            arr[m] = [0,1,0,1,0,1,0,1] # Makes even rows follow this pattern.
        if m % 2 != 0: 
             arr[m] = [1,0,1,0,1,0,1,0]
    return arr

print(checkerboard_evenrows())

# Question 2.4

def reversed_checkerboard():
    arr = np.zeros((8,8)) # Makes an 8x8 filled with zeroes.
    for m in range(8): # Tells Python to look at the rows
        if m % 2 == 0: # Identifies the even rows.
            arr[m] = [1,0,1,0,1,0,1,0] # Makes even rows follow this pattern.
        if m % 2 != 0: 
             arr[m] = [0,1,0,1,0,1,0,1]
    return arr

print(reversed_checkerboard())

# Question 3

import numpy as np

def expansion(universe, n):
    return np.array([(" " * n).join(universe) for word in universe])

universe = np.array(['galaxy', 'clusters'])
print(expansion(universe, 1))
print(expansion(universe, 2))

# Question 4
import numpy as np

def secondDimmest(stars):
    return np.sort(stars, axis = 0)[1]
np.random.seed(123)
stars = np.random.randint(500, 2000, (5, 5))
print(secondDimmest(stars))
