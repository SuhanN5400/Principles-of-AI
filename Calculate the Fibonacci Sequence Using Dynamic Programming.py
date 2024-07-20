def fibonacci_dynamic(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib

n = 10
print("Fibonacci sequence:", fibonacci_dynamic(n))
