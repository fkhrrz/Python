def fibonacci(e):
    output = ""
    for x in range(e):
        if x <= 1:
            a = 0
            b = x
            output += str(b) + ' '
        else:
            output += str(a + b) + ' '
            temp = a
            a = b
            b = a + temp
    return output

print(fibonacci(16))