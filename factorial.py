def factorial(n):
    if n<0:
        return "factorial is not define for 0 and negative numbers "
    result=1
    for i in range (1, n+1):
        result=result*i
    return result
n=int(input("Enter a number :"))

print(f"The factorial of {n} is :{factorial(n)}")