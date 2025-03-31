
# Question 1.1
    # pwd would tell you what your working directory is

# Question 1.2
    # ls shows you all the files in your current directory

# Question 1.3
    # cd = change directory (name) and then git pull (to see latest changes)

# Question 1.4
    # mv (homework.py) --> (designated folder you wanna move it to)

# Question 1.5
    # open l

# Question 1.6
    # cp = access into file

# Question 1.7 
    # .git add --> git push

# Question 1.8
    # Because you are trying to push a file to main folder that is already in main folder. 

# Question 1.9
    # Just a slash (/) by itself will take you to the absolute path.


# Question 2.1
def checkdatatype(x):
    return type(x).__name__

print(checkdatatype(3.14))
print(checkdatatype(True))

# Question 2.2
def evenorodd(x):
    if x % 2 == 0:
        return "even"
    else:
        return "odd"
x = 10
print(evenorodd(x))

# Question 3
def sumwithloop(numbers):
    total = 0
    for num in numbers: #iterates through the list
        total += num #adds the numbers in the list to total (which we defined as 0)
    return total
numbers = [1,2,3,4,5]
print(sumwithloop(numbers))

#Question 4.1
def duplicateList(input_list):
    result = [] #initalizes an empty list to store our results
    for item in input_list:
        result.append(item) #do it once to add this to the result list
        result.append(item) #do it again to duplicate the element in the result list.
    return result
input_list = ['a','b','c']
print(duplicateList(input_list))

#Question 4.2
def square(num):
    return num * num

#These two lines below are missing.
num = 2
print(square(num))

