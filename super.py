class A:
    def MyMethod(self):
        print("This is class  A")

class B:
    def MyMethod(self):
        print("This is class B")

class C:
    def MyMethod(self):
        print("This is class C")

class D(A,C,B):
    def MyMethod(self):
        print("This is class D")
        super().MyMethod()


def main():

    obj=D()
    obj.MyMethod()

if __name__=="__main__":
        main()

        
        
