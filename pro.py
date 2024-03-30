#Data types : 
#Operators : 
#Looping :
#Function : 
#lambda : Anonymous function

# def displayData(): #Function declaration
#     pass 


# displayData()  #Function calling


# def displayData(name, age):
#     print(f'Welcome {name} your age is {age} years')


# displayData("Divya", 24,50000)

# ls = [1,2,3,4,5,6,7,8,9]
# def additionNumber(x,y,z):
#     return x + y + z 

# result = additionNumber(25,25,25)
# print(f'Addition of numbers are : {result}')


# ls = [1,2,3,4,5,6,7,8,9]
# def additionNumber(*args):
#     return sum(args) 

# result = additionNumber(25,25,25,25,45,4,5,4,54)
# print(f'Addition of numbers are : {result}')

# The args stands for arguments that are passed to the function whereas kwargs stands for keyword arguments which are passed along with the values into the function. We will learn about these special symbols in this article.

# def displayData(name="Ram", age=21, salary=25000):
#     print(f'Welcome {name} your age is {age} years with salary {salary}')


#  displayData("Divya", 24,50000)
    
    
# displayData()

# ls = [2,3,4,5,6,7,8,9]
# def additionNumber(*args):
#     return sum(args)


# result = additionNumber(*ls)

# print(f'Addition is : {result}')

# def displayData(*args):
#     res = 1
#     for i in args:
#         res = res * i
#     return res

# result = displayData(25,25)

# print(result)

# def calculated_sum(*args):
#     total = 0
#     for num in args:
#         total = total + num 
#     return total 

# result = calculated_sum(10,20,30,40)
# print(f'Addition is : {result}')

# n = int(input("Enter the number : "))
# count = 0
# for i in range(2,n):
#     if(n%i==0):
#         count += 1
# if(count == 0):
#     print("Prime number")
# else:
#     print("Not prime")