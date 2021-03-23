#An algorithm is said to have an exponential time complexity when the growth doubles with each addition
# to the input data set. This kind of time complexity is usually seen in brute-force algorithms.


# example of an exponential time algorithm is the recursive calculation of Fibonacci numbers:
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(10))