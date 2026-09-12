# def average(a,b,c):
#     d = (a+b+c)/3
#     return d
# print(average(10,20,30))


def add(a,b,plus = 0):
    c = a+ b+plus
    return c 
d =add(30,56,34)
print(d)

d1 = add(b=50 , a=34)
print(d1)


def num(n):
    if n == 0:
        return
    num(n-1)
    print(n)
num