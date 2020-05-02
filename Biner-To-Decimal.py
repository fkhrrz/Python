def bindec(f):
    f = f[::-1]
    result = 0
    for x in range(len(f)):
        if f[x] == '1':
            result += 2 ** x
    return result
print(bindec("01010110"))