def foo(a, b):
    if a+b in range(10, 15):
        return 20
    else:
        return a+b
x=foo(9, 5)
y=foo(9,6)
print(foo(x, y))

