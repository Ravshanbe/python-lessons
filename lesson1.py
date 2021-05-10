# a=list(range(10))
# b=list(map(lambda x:x**2,a))
# print(b)
def power(n):
    return lambda x:x**n
kvadrat=power(2)
kub=power(3)
print(kub(2))
