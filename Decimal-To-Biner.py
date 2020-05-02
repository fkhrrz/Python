def decbin(f):
    if f == 0:
        return "0"
    else:
        return str(decbin(f//2)) + str(f % 2)
print(decbin(11))