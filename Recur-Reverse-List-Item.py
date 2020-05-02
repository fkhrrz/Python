def listReverse(l):
    if len(l) == 0:
        return []
    return [l[-1]] + listReverse(l[:-1])

print(listReverse([1,6,13,8,4,9]))