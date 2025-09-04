# Fibonacci sequence
def fibonacci(n):
    a, b = 0, 1
    fibonacci_sequence = [0]
    for _ in range(n):
        fibonacci_sequence.append(a)
        a, b = b, a + b
    return fibonacci_sequence


print(fibonacci(10))
