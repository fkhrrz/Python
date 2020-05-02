def grader(c,d):
    if d == 1:
        return c
    else:
        return c * grader(c,(d-1))
print(grader(2,10))