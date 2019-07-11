def make_pretty(func):
    def inner():
        print("This is inner function inside make_pretty()")
        func()
        return inner()
#@make_pretty
def ordinary():
    print("This is Ordinary Function")
make_pretty(ordinary)
print(ordinary())
print(make_pretty())




