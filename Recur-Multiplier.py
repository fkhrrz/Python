def multiplier(a,b):
    if b == 1:
        return a
    else:
        return a + multiplier(a,(b-1))
print(multiplier(8,8))