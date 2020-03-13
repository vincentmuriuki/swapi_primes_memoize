def memoize(func):
    data = {}
    def helperfunc(x):
        if x not in data:
            data[x] = func(x)
        return data[x]
    return helperfunc

@memoize
def is_prime(number):
    if number > 1:
        for i in range(2, number):
            if (i % number == 0):
                return False
        else:
            return True
    else:
        return False


a = is_prime(3)
b = is_prime(47)
c = is_prime(1)
d = is_prime(35)

print(a)
print(b)
print(c)
print(d)