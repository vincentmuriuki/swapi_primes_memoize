# Write a function called memoize that takes any other function as input and returns a memoized version of that function

def memoize(func):
    data = {}
    def helperfunc(x):
        if x not in data:
            data[x] = func(x)
        return data[x]
    return helperfunc