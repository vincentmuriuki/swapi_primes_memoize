def memoize(func):
    data = {}
    def helper(x):
        if x not in data:
            data[x] = func(x)
        return data[x]
    return helper