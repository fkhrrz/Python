def fibonacci(e):
    if e <= 1:
        result = e
    else:
        result = fibonacci(e-1) + fibonacci(e-2)
    return result

for x in range(16):
    print(fibonacci(x), end=' ')