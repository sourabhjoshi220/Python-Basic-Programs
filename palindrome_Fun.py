def palindrome(a):
    x=str(a)
    print(x)
    rev_a= x[::-1]
    if x==rev_a:
        return True
    else:
        return False


print(palindrome(a=121))


