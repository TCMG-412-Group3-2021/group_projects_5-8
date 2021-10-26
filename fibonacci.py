
 
def Fibonacci(n):
    if n<0:
        print("Error!!")
    # 1st Fibonacci number is 0
    elif n==0:
        return 0
    # 2nd Fibonacci number is 1
    elif n==1:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)
 
# Driver Program
 
print(Fibonacci(7))
