def getMax(item):
    if len(item) == 1:
        return item[0]
    else:
        m = getMax(item[1:])
        return m if m > item[0] else item[0]

print(getMax([1,6,13,8,4,9]))